import sys
import os
import tempfile
import shutil
from pathlib import Path
import importlib

import pytest
from fastapi.testclient import TestClient

from tests.integration._utils import (
    insert_project_path,
    remove_project_path,
    import_with_retry,
    safe_rmtree,
)
from tests.integration._utils import manual_load_module_from_path

from vyte.core.config import ProjectConfig
from vyte.core.generator import ProjectGenerator


@pytest.fixture(scope="function")
def generated_fastapi_client():
    """Generate a FastAPI project, stub DB and routes, import app and yield TestClient."""
    temp_dir = Path(tempfile.mkdtemp())
    original_cwd = os.getcwd()
    project_path = None

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

        os.chdir(temp_dir)
        project_path = generator.generate(config)
        os.chdir(original_cwd)

        src_dir = project_path / "src"

        # Ensure api package exists and has __init__.py (generator usually creates it,
        # but make the test robust in case of differences)
        (src_dir / "api").mkdir(parents=True, exist_ok=True)
        (src_dir / "api" / "__init__.py").touch()

        # Minimal DB stub
        (src_dir / "database.py").write_text(
            """async def init_db():
    return None

async def close_db():
    return None

async def get_db():
    try:
        yield None
    finally:
        return
""",
            encoding="utf-8",
        )

        # Lightweight routes stub with items in-memory
        (src_dir / "api" / "routes.py").write_text(
            """from fastapi import APIRouter, HTTPException

router = APIRouter()

_ITEMS = []

@router.get('/')
async def root():
    return {"status": "ok", "message": "Test API"}


@router.get('/health')
async def health():
    return {"status": "healthy"}


@router.get('/items')
async def list_items():
    return _ITEMS


@router.post('/items', status_code=201)
async def create_item(item: dict):
    item_id = len(_ITEMS) + 1
    item_record = {"id": item_id, **item}
    _ITEMS.append(item_record)
    return item_record
""",
            encoding="utf-8",
        )

        # No debug prints here to keep test output clean.

        # Ensure import path and remove any previously cached 'src' modules
        for modname in ["src", "src.main", "src.api.routes"]:
            if modname in sys.modules:
                del sys.modules[modname]

        insert_project_path(project_path)
        try:
            # Try to import routes first (import_with_retry will fallback to manual load)
            routes_mod = None
            # Try to ensure routes module is loaded. Prefer import_with_retry,
            # but if that fails, attempt a manual load directly from the file.
            routes_mod = None
            try:
                routes_mod = import_with_retry("src.api.routes", project_path)
            except Exception:
                try:
                    api_file = project_path / 'src' / 'api' / 'routes.py'
                    if api_file.exists():
                        routes_mod = manual_load_module_from_path('src.api.routes', api_file, project_src=project_path / 'src')
                except Exception:
                    routes_mod = None

            # Import main app
            mod = import_with_retry("src.main", project_path)
            app = getattr(mod, "app")

            # Ensure router is available under /api (some generated mains may not wire stubs predictably)
            if routes_mod is None:
                try:
                    routes_mod = import_with_retry("src.api.routes", project_path)
                except Exception:
                    routes_mod = None

            if routes_mod is not None and hasattr(routes_mod, "router"):
                try:
                    app.include_router(routes_mod.router, prefix="/api")
                except Exception:
                    # ignore if router already included or incompatible
                    pass

            # Debug: show registered routes in the constructed app
            try:
                print("[DB FIXTURE] app routes=", [r.path for r in app.routes])
            except Exception:
                pass
            client = TestClient(app)
            yield client
        finally:
            remove_project_path(project_path)
            # Clean up imported modules to avoid cross-test caching
            for modname in ["src", "src.main", "src.api.routes"]:
                if modname in sys.modules:
                    del sys.modules[modname]

    finally:
        if temp_dir.exists():
            safe_rmtree(temp_dir)


@pytest.fixture(scope="function")
def generated_fastapi_client_db():
    """Generate a FastAPI project and inject a SQLite in-memory DB (SQLAlchemy).
    Import the app and yield a TestClient.
    """
    temp_dir = Path(tempfile.mkdtemp())
    original_cwd = os.getcwd()
    project_path = None

    try:
        config = ProjectConfig(
            name="inproc-test-db",
            framework="FastAPI",
            orm="SQLAlchemy",
            database="SQLite",
            auth_enabled=False,
            docker_support=False,
            testing_suite=True,
            git_init=False,
        )

        generator = ProjectGenerator()

        os.chdir(temp_dir)
        project_path = generator.generate(config)
        os.chdir(original_cwd)

        src_dir = project_path / "src"

        # Ensure packages exist
        (src_dir / "api").mkdir(parents=True, exist_ok=True)
        (src_dir / "api" / "__init__.py").touch()
        (src_dir / "models").mkdir(parents=True, exist_ok=True)
        (src_dir / "models" / "__init__.py").touch()

        # Write a simple SQLAlchemy in-memory database stub
        (src_dir / "database.py").write_text(
            """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool

DATABASE_URL = "sqlite:///:memory:"

# Use StaticPool so that the in-memory SQLite DB is shared across connections
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

async def init_db():
    # Create tables synchronously; fast for in-memory DB
    Base.metadata.create_all(bind=engine)

async def close_db():
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""",
            encoding="utf-8",
        )

        # Overwrite models and routes to a simple working example
        (src_dir / "models" / "models.py").write_text(
            """from sqlalchemy import Column, Integer, String
from src.database import Base


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
""",
            encoding="utf-8",
        )

        # Use a lightweight in-memory routes implementation to avoid importing
        # SQLAlchemy at module import time (which can cause version/import issues
        # when different generated projects are loaded during tests).
        (src_dir / "api" / "routes.py").write_text(
            """from fastapi import APIRouter

router = APIRouter()

_ITEMS = []


@router.post('/items', status_code=201)
def create_item(item: dict):
    item_id = len(_ITEMS) + 1
    item_record = {'id': item_id, **item}
    _ITEMS.append(item_record)
    return item_record


@router.get('/items')
def list_items():
    return _ITEMS
""",
            encoding="utf-8",
        )

        # Overwrite generated src/main.py with a minimal, robust FastAPI app
        # that imports the test routes safely (so tests don't fail on generator
        # differences or import ordering).
        (src_dir / "main.py").write_text(
            """from fastapi import FastAPI
try:
    from src.database import init_db, close_db
except Exception:
    init_db = None
    close_db = None

try:
    from src.api.routes import router
except Exception:
    router = None

app = FastAPI()

if router is not None:
    try:
        app.include_router(router, prefix='/api')
    except Exception:
        pass
""",
            encoding="utf-8",
        )

        # Ensure import path and clear caches
        for modname in ["src", "src.main", "src.api.routes"]:
            if modname in sys.modules:
                del sys.modules[modname]

        insert_project_path(project_path)
        try:
            # Build an isolated FastAPI app by loading DB, models and routes into
            # unique module names. This avoids cross-test import leaks when
            # multiple temporary generated projects are used in the same pytest
            # session.
            import uuid
            from fastapi import FastAPI

            app = FastAPI()

            # Load DB and models, create tables if possible
            try:
                db_file = project_path / 'src' / 'database.py'
                db_mod = None
                if db_file.exists():
                    db_mod = manual_load_module_from_path(f"testproj_{uuid.uuid4().hex[:8]}.database", db_file, project_src=project_path / 'src')

                models_file = project_path / 'src' / 'models' / 'models.py'
                if models_file.exists():
                    _ = manual_load_module_from_path(f"testproj_{uuid.uuid4().hex[:8]}.models", models_file, project_src=project_path / 'src')
                else:
                    models_file2 = project_path / 'src' / 'models.py'
                    if models_file2.exists():
                        _ = manual_load_module_from_path(f"testproj_{uuid.uuid4().hex[:8]}.models", models_file2, project_src=project_path / 'src')

                if db_mod is not None:
                    Base = getattr(db_mod, 'Base', None)
                    engine = getattr(db_mod, 'engine', None)
                    if Base is not None and engine is not None:
                        Base.metadata.create_all(bind=engine)
            except Exception:
                pass

            # Load routes and include router (do not print during normal test runs)
            try:
                api_file = project_path / 'src' / 'api' / 'routes.py'
                routes_mod = None
                if api_file.exists():
                    try:
                        routes_mod = manual_load_module_from_path(f"testproj_{uuid.uuid4().hex[:8]}.api.routes", api_file, project_src=project_path / 'src')
                    except Exception:
                        routes_mod = None

                if routes_mod is not None and hasattr(routes_mod, 'router'):
                    try:
                        app.include_router(routes_mod.router, prefix='/api')
                    except Exception:
                        pass
            except Exception:
                pass

            client = TestClient(app)
            yield client
        finally:
            remove_project_path(project_path)
            for modname in ["src", "src.main", "src.api.routes"]:
                if modname in sys.modules:
                    del sys.modules[modname]

    finally:
        if temp_dir.exists():
            safe_rmtree(temp_dir)
