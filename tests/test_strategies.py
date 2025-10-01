# tests/test_strategies.py
"""
Test strategy pattern implementations
"""

from rdt.core.config import ProjectConfig
from rdt.core.renderer import TemplateRenderer
from rdt.strategies.flask_restx import FlaskRestxStrategy
from rdt.strategies.fastapi import FastAPIStrategy


def test_flask_strategy():
    """Test Flask-Restx strategy"""
    config = ProjectConfig(
        name="test-flask",
        framework="Flask-Restx",
        orm="SQLAlchemy",
        database="PostgreSQL",
    )

    renderer = TemplateRenderer()
    strategy = FlaskRestxStrategy(config, renderer)

    assert strategy.config == config
    assert strategy.renderer == renderer


def test_fastapi_strategy():
    """Test FastAPI strategy"""
    config = ProjectConfig(
        name="test-fastapi",
        framework="FastAPI",
        orm="SQLAlchemy",
        database="PostgreSQL",
    )

    renderer = TemplateRenderer()
    strategy = FastAPIStrategy(config, renderer)

    assert strategy.config == config
    assert strategy.renderer == renderer
