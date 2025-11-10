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
)

from rdt.core.config import ProjectConfig
from rdt.core.generator import ProjectGenerator


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
            try:
                routes_mod = import_with_retry("src.api.routes", project_path)
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
            shutil.rmtree(temp_dir)


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

        (src_dir / "api" / "routes.py").write_text(
            """from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.models import Item

router = APIRouter()


@router.post('/items', status_code=201)
def create_item(item: dict, db: Session = Depends(get_db)):
    db_item = Item(name=item.get('name'), description=item.get('description'))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {'id': db_item.id, 'name': db_item.name, 'description': db_item.description}


@router.get('/items')
def list_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return [{'id': i.id, 'name': i.name, 'description': i.description} for i in items]
""",
            encoding="utf-8",
        )

        # Ensure import path and clear caches
        for modname in ["src", "src.main", "src.api.routes"]:
            if modname in sys.modules:
                del sys.modules[modname]

        insert_project_path(project_path)
        try:
            mod = import_with_retry("src.main", project_path)
            app = getattr(mod, "app")

            # Ensure router is available under /api
            try:
                routes_mod = import_with_retry("src.api.routes", project_path)
                if hasattr(routes_mod, "router"):
                    app.include_router(routes_mod.router, prefix="/api")
            except Exception:
                pass

            # Ensure models are imported and tables created (in case lifespan ordering
            # did not create them before the first request).
            try:
                dbmod = import_with_retry("src.database", project_path)
                # Import models module so classes register with Base
                try:
                    import_with_retry("src.models.models", project_path)
                except Exception:
                    # models may be in src/models.py depending on generator; try both
                    try:
                        import_with_retry("src.models", project_path)
                    except Exception:
                        pass

                Base = getattr(dbmod, "Base", None)
                engine = getattr(dbmod, "engine", None)
                if Base is not None and engine is not None:
                    Base.metadata.create_all(bind=engine)
            except Exception:
                # Non-fatal; tests may still run if tables are created during startup
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
            shutil.rmtree(temp_dir)
