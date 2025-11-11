"""Helpers for integration tests.

Provide small utilities to generate projects, write stubs, manage sys.path and
manually load modules when filesystem timing causes flaky imports on CI/Windows.
"""
from pathlib import Path
import sys
import importlib
import types
import time
from typing import Optional
import time
import os
import stat


def safe_rmtree(path):
    """Remove a directory tree with retries and an onerror handler for Windows locks."""
    p = str(path)
    for _ in range(5):
        try:
            shutil.rmtree(p)
            return
        except Exception:
            time.sleep(0.1)
    # Last attempt with onerror to clear read-only flags
    def _onerror(func, path, excinfo):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception:
            pass

    try:
        shutil.rmtree(p, onerror=_onerror)
    except Exception:
        pass


def insert_project_path(project_path: Path) -> None:
    p = str(project_path)
    if p not in sys.path:
        sys.path.insert(0, p)


def remove_project_path(project_path: Path) -> None:
    p = str(project_path)
    try:
        sys.path.remove(p)
    except ValueError:
        pass


def manual_load_module_from_path(module_name: str, file_path: Path, project_src: Optional[Path] = None) -> types.ModuleType:
    """Manually load a module from a file and insert it into sys.modules.

    Ensures `src` and `src.api` packages exist in sys.modules with __path__ set
    so subsequent imports treat them as packages.
    """
    if project_src is None:
        # file_path is expected to be like <project_path>/src/...py
        # project_src should point to the project's `src` directory so
        # package __path__ entries resolve correctly.
        project_src = file_path.parent

    # Ensure package entries
    pkg_root_name = module_name.split('.')[0]
    if pkg_root_name not in sys.modules:
        pkg_root = types.ModuleType(pkg_root_name)
        pkg_root.__path__ = [str(project_src)]
        sys.modules[pkg_root_name] = pkg_root

    # Add intermediate packages if needed
    parts = module_name.split('.')
    for i in range(2, len(parts)):
        pkg_name = '.'.join(parts[:i])
        pkg_path = project_src / '/'.join(parts[1:i])
        if pkg_name not in sys.modules:
            pkg = types.ModuleType(pkg_name)
            # Try to set __path__ if we can
            pkg.__path__ = [str(project_src / '/'.join(parts[1:i]))]
            sys.modules[pkg_name] = pkg
    # Preload common nested modules that generated mains often import (e.g. src.api.routes)
    try:
        api_routes = project_src / 'api' / 'routes.py'
        if api_routes.exists() and f"{pkg_root_name}.api.routes" not in sys.modules:
            # Load routes module so imports inside main succeed
            manual_load_module_from_path(f"{pkg_root_name}.api.routes", api_routes, project_src=project_src)
    except Exception:
        # Non-fatal; continue to load requested module
        pass

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    module = types.ModuleType(module_name)
    module.__file__ = str(file_path)
    exec(compile(code, str(file_path), 'exec'), module.__dict__)
    sys.modules[module_name] = module
    # Ensure parent package objects expose the child as an attribute so
    # statements like `from src.api import routes` work as expected when
    # modules were injected into sys.modules manually.
    if "." in module_name:
        parent_name, child_name = module_name.rsplit('.', 1)
        parent = sys.modules.get(parent_name)
        if parent is not None:
            try:
                setattr(parent, child_name, module)
            except Exception:
                # Non-fatal: ignore if we cannot set attribute
                pass

    return module


def import_with_retry(module_name: str, project_path: Path, retries: int = 3, backoff: float = 0.05):
    """Try to import a module from a generated project path; fall back to manual load.

    Returns the imported module or raises the last exception.
    """
    insert_project_path(project_path)
    last_exc = None
    for _ in range(retries):
        try:
            return importlib.import_module(module_name)
        except ModuleNotFoundError as e:
            last_exc = e
            time.sleep(backoff)
    # Fallback: manual load if module looks like a file inside the project
    parts = module_name.split('.')
    # Construct path assuming module corresponds to project/src/... .py
    if parts[0] == 'src' and len(parts) >= 2:
        rel = Path('src') / Path('/'.join(parts[1:]) + '.py')
        candidate = project_path / rel
        # If main imports auxiliary modules (like src.api.routes), try to preload them
        try:
            api_candidate = project_path / 'src' / 'api' / 'routes.py'
            if api_candidate.exists() and 'src.api.routes' not in sys.modules:
                # Preload routes so manual-loading main won't fail on imports
                manual_load_module_from_path('src.api.routes', api_candidate, project_src=project_path / 'src')
        except Exception:
            pass
        if candidate.exists():
            return manual_load_module_from_path(module_name, candidate, project_src=project_path / 'src')
    raise last_exc
