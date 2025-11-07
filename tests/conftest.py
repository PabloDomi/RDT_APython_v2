# tests/conftest.py
"""
Pytest configuration and fixtures
"""
import pytest
from pathlib import Path
import shutil
import tempfile

from rdt.core.config import ProjectConfig
from rdt.core.generator import ProjectGenerator
from rdt.core.renderer import TemplateRenderer
from click.testing import CliRunner


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests"""
    temp = Path(tempfile.mkdtemp())
    yield temp
    if temp.exists():
        shutil.rmtree(temp)


@pytest.fixture
def sample_config():
    """Sample project configuration"""
    return ProjectConfig(
        name="test-api",
        framework="Flask-Restx",
        orm="SQLAlchemy",
        database="PostgreSQL",
        auth_enabled=True,
        docker_support=True,
        testing_suite=True,
        git_init=False,
    )


@pytest.fixture
def generator():
    """Project generator instance"""
    return ProjectGenerator()


@pytest.fixture
def renderer():
    """Template renderer instance"""
    return TemplateRenderer()


@pytest.fixture
def runner():
    """Reusable Click CLI test runner"""
    return CliRunner()