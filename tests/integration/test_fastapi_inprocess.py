import importlib
import os
import sys
import tempfile
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from tests.integration._utils import safe_rmtree
from vyte.core.config import ProjectConfig
from vyte.core.generator import ProjectGenerator


@pytest.mark.integration
@pytest.mark.slow
def test_generated_fastapi_inprocess_root_and_health():
    """Generate a FastAPI project, stub DB, import app and test / and /health endpoints."""
    temp_dir = Path(tempfile.mkdtemp())

    try:
        config = ProjectConfig(
            name="inproc-test",
            framework="FastAPI",
            orm="SQLAlchemy",
            database="SQLite",
            auth_enabled=False,
            docker_support=False,
            testing_suite=True,
            git_init=False,
        )

        generator = ProjectGenerator()

        # Generate project into temp dir
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        try:
            project_path = generator.generate(config)
        finally:
            os.chdir(original_cwd)

        # Ensure import path contains the generated project root so `src` package imports work
        src_dir = project_path / "src"
        sys.path.insert(0, str(project_path))

        # Create a minimal stub src/database.py to avoid real DB init on import
        db_stub = src_dir / "database.py"
        db_stub.write_text(
            """async def init_db():
    return None

async def close_db():
    return None

async def get_db():
    # async generator yielding a dummy value
    try:
        yield None
    finally:
        return
""",
            encoding="utf-8",
        )

        # Replace generated api/routes.py with a lightweight stub to avoid importing models
        api_dir = src_dir / "api"
        # Ensure api package exists so writing files won't fail on some filesystems/CI
        api_dir.mkdir(parents=True, exist_ok=True)
        (api_dir / "__init__.py").touch()
        routes_stub = api_dir / "routes.py"
        routes_stub.write_text(
            """from fastapi import APIRouter

router = APIRouter()

@router.get('/stub-health')
async def stub_health():
    return {"status": "healthy"}
""",
            encoding="utf-8",
        )

        try:
            # Ensure src.api.routes is importable (some platforms/filesystems may be flaky)
            try:
                importlib.import_module("src.api.routes")
            except ModuleNotFoundError:
                # Manually load the stub module into sys.modules
                import types

                routes_path = src_dir / "api" / "routes.py"
                module_name = "src.api.routes"
                if "src" not in sys.modules:
                    pkg_root = types.ModuleType("src")
                    pkg_root.__path__ = [str(project_path / "src")]
                    sys.modules["src"] = pkg_root
                if "src.api" not in sys.modules:
                    pkg = types.ModuleType("src.api")
                    pkg.__path__ = [str(project_path / "src" / "api")]
                    sys.modules["src.api"] = pkg

                with open(routes_path, encoding="utf-8") as f:
                    code = f.read()
                module = types.ModuleType(module_name)
                module.__file__ = str(routes_path)
                exec(compile(code, str(routes_path), "exec"), module.__dict__)
                sys.modules[module_name] = module

            # Import the generated FastAPI app
            mod = importlib.import_module("src.main")
            app = mod.app

            client = TestClient(app)

            r = client.get("/")
            assert r.status_code == 200
            assert "status" in r.json()

            r2 = client.get("/health")
            assert r2.status_code == 200
            assert r2.json().get("status") in ("healthy", "ok")

        finally:
            # cleanup sys.path
            try:
                sys.path.remove(str(project_path))
            except ValueError:
                pass

    finally:
        if temp_dir.exists():
            safe_rmtree(temp_dir)
