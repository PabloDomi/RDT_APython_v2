# API Reference

Complete API reference for Vyte's Python API. This page documents all public classes, functions, and interfaces.

## Installation

```bash
pip install vyte
```

______________________________________________________________________

## Core Modules

### vyte.core.generator

The main project generator module.

#### ProjectGenerator

```python
from vyte.core.generator import ProjectGenerator


class ProjectGenerator:
    """
    Main class for generating API projects from templates.

    Attributes:
        project_name (str): Name of the project to generate
        framework (str): Web framework to use
        orm (str): ORM to use
        database (str): Database type
        output_dir (Path): Directory where project will be created
    """

    def __init__(
        self,
        project_name: str,
        framework: str,
        orm: str,
        database: str,
        output_dir: str | Path = ".",
    ):
        """
        Initialize the project generator.

        Args:
            project_name: Name for the new project
            framework: "FastAPI", "Flask-Restx", or "Django-Rest"
            orm: "SQLAlchemy", "TortoiseORM", or "Peewee"
            database: "PostgreSQL", "MySQL", or "SQLite"
            output_dir: Parent directory for the project

        Raises:
            ValueError: If invalid framework/orm/database combination
        """
        pass

    def generate(self) -> Path:
        """
        Generate the complete project structure.

        Returns:
            Path: Path to the generated project directory

        Raises:
            FileExistsError: If project directory already exists
            ValidationError: If configuration is invalid
        """
        pass
```

**Example Usage:**

```python
from vyte.core.generator import ProjectGenerator

generator = ProjectGenerator(
    project_name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
)

project_path = generator.generate()
print(f"Project created at: {project_path}")
```

______________________________________________________________________

### vyte.core.config

Configuration management and validation.

#### ProjectConfig

```python
from vyte.core.config import ProjectConfig


class ProjectConfig:
    """
    Configuration container for project generation.

    Attributes:
        project_name (str): Project name
        framework (str): Selected framework
        orm (str): Selected ORM
        database (str): Selected database
        python_version (str): Target Python version
        use_alembic (bool): Include Alembic migrations
        use_docker (bool): Generate Dockerfile
        use_tests (bool): Include test suite
    """

    @classmethod
    def from_interactive(cls) -> "ProjectConfig":
        """
        Create configuration through interactive prompts.

        Returns:
            ProjectConfig: Validated configuration
        """
        pass

    def validate(self) -> bool:
        """
        Validate the configuration.

        Returns:
            bool: True if valid

        Raises:
            ValidationError: If configuration is invalid
        """
        pass
```

**Example Usage:**

```python
from vyte.core.config import ProjectConfig

# Interactive mode
config = ProjectConfig.from_interactive()

# Manual configuration
config = ProjectConfig(
    project_name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
    use_alembic=True,
    use_docker=True,
)

# Validate before generating
if config.validate():
    print("Configuration is valid!")
```

______________________________________________________________________

### vyte.core.dependencies

Dependency resolution and management.

#### DependencyManager

```python
from vyte.core.dependencies import DependencyManager


class DependencyManager:
    """
    Manages project dependencies based on selected stack.

    Determines required Python packages based on framework,
    ORM, and database choices.
    """

    def __init__(self, config: ProjectConfig):
        """
        Initialize dependency manager.

        Args:
            config: Project configuration
        """
        pass

    def get_dependencies(self) -> dict[str, list[str]]:
        """
        Get all project dependencies.

        Returns:
            dict: Dependencies grouped by category
                - "core": Framework and core dependencies
                - "database": Database drivers and ORM
                - "dev": Development dependencies
                - "test": Testing dependencies
        """
        pass

    def get_requirements(self) -> str:
        """
        Generate requirements.txt content.

        Returns:
            str: Formatted requirements file content
        """
        pass
```

**Example Usage:**

```python
from vyte.core.config import ProjectConfig
from vyte.core.dependencies import DependencyManager

config = ProjectConfig(
    project_name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
)

dep_manager = DependencyManager(config)

# Get all dependencies
deps = dep_manager.get_dependencies()
print(deps["core"])  # ['fastapi>=0.104.0', 'uvicorn[standard]>=0.24.0']

# Generate requirements.txt
requirements = dep_manager.get_requirements()
```

______________________________________________________________________

### vyte.core.renderer

Template rendering engine.

#### TemplateRenderer

```python
from vyte.core.renderer import TemplateRenderer


class TemplateRenderer:
    """
    Renders Jinja2 templates with project configuration.

    Handles template loading, context preparation, and file generation.
    """

    def __init__(self, config: ProjectConfig):
        """
        Initialize template renderer.

        Args:
            config: Project configuration
        """
        pass

    def render_template(
        self, template_name: str, context: dict[str, Any] | None = None
    ) -> str:
        """
        Render a template to string.

        Args:
            template_name: Name of template file
            context: Additional context variables

        Returns:
            str: Rendered template content
        """
        pass

    def render_to_file(
        self,
        template_name: str,
        output_path: Path,
        context: dict[str, Any] | None = None,
    ) -> None:
        """
        Render template and write to file.

        Args:
            template_name: Name of template file
            output_path: Where to write rendered content
            context: Additional context variables
        """
        pass
```

**Example Usage:**

```python
from pathlib import Path
from vyte.core.config import ProjectConfig
from vyte.core.renderer import TemplateRenderer

config = ProjectConfig(
    project_name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
)

renderer = TemplateRenderer(config)

# Render to string
content = renderer.render_template(
    "fastapi/main.py.j2", context={"app_title": "My Amazing API"}
)

# Render to file
renderer.render_to_file(
    "fastapi/main.py.j2",
    Path("my-api/app/main.py"),
    context={"app_title": "My Amazing API"},
)
```

______________________________________________________________________

### vyte.core.alembic_setup

Alembic migration setup utilities.

#### AlembicSetup

```python
from vyte.core.alembic_setup import AlembicSetup


class AlembicSetup:
    """
    Sets up Alembic migrations for the project.
    """

    @staticmethod
    def initialize(
        project_path: Path, database_url: str, base_class: str = "Base"
    ) -> None:
        """
        Initialize Alembic in the project.

        Args:
            project_path: Root directory of the project
            database_url: Database connection string
            base_class: SQLAlchemy declarative base class name
        """
        pass

    @staticmethod
    def generate_env_py(project_path: Path, config: ProjectConfig) -> str:
        """
        Generate alembic/env.py content.

        Args:
            project_path: Root directory of the project
            config: Project configuration

        Returns:
            str: Generated env.py content
        """
        pass
```

**Example Usage:**

```python
from pathlib import Path
from vyte.core.alembic_setup import AlembicSetup

project_path = Path("my-api")

AlembicSetup.initialize(
    project_path=project_path,
    database_url="postgresql://user:pass@localhost/db",
    base_class="Base",
)
```

______________________________________________________________________

## Strategy Modules

### vyte.strategies.base

Base strategy interface.

#### BaseStrategy

```python
from vyte.strategies.base import BaseStrategy


class BaseStrategy(ABC):
    """
    Abstract base class for framework strategies.

    Each framework implements this interface to define
    how projects are generated for that framework.
    """

    @abstractmethod
    def generate_structure(self, project_path: Path) -> None:
        """
        Generate the project directory structure.

        Args:
            project_path: Root directory for the project
        """
        pass

    @abstractmethod
    def generate_files(self, project_path: Path) -> None:
        """
        Generate all project files from templates.

        Args:
            project_path: Root directory for the project
        """
        pass

    @abstractmethod
    def validate_compatibility(self) -> bool:
        """
        Validate framework/ORM/database compatibility.

        Returns:
            bool: True if combination is supported
        """
        pass
```

______________________________________________________________________

### vyte.strategies.fastapi

FastAPI-specific strategy.

#### FastAPIStrategy

```python
from vyte.strategies.fastapi import FastAPIStrategy


class FastAPIStrategy(BaseStrategy):
    """
    Generation strategy for FastAPI projects.

    Supports:
    - SQLAlchemy (async and sync)
    - TortoiseORM (async)
    - All databases
    """

    def generate_structure(self, project_path: Path) -> None:
        """Generate FastAPI project structure."""
        pass

    def generate_files(self, project_path: Path) -> None:
        """Generate FastAPI-specific files."""
        pass

    def validate_compatibility(self) -> bool:
        """Validate FastAPI compatibility."""
        pass
```

______________________________________________________________________

### vyte.strategies.flask_restx

Flask-Restx-specific strategy.

#### FlaskRestxStrategy

```python
from vyte.strategies.flask_restx import FlaskRestxStrategy


class FlaskRestxStrategy(BaseStrategy):
    """
    Generation strategy for Flask-Restx projects.

    Supports:
    - SQLAlchemy (sync)
    - Peewee (SQLite only)
    """

    def generate_structure(self, project_path: Path) -> None:
        """Generate Flask-Restx project structure."""
        pass

    def generate_files(self, project_path: Path) -> None:
        """Generate Flask-Restx-specific files."""
        pass

    def validate_compatibility(self) -> bool:
        """Validate Flask-Restx compatibility."""
        pass
```

______________________________________________________________________

## Utility Modules

### vyte.utils.logger

Logging utilities.

```python
from vyte.utils.logger import get_logger, setup_logging

# Get logger instance
logger = get_logger(__name__)
logger.info("Project generation started")

# Setup logging configuration
setup_logging(level="DEBUG", format="json")
```

______________________________________________________________________

### vyte.utils.git

Git integration utilities.

```python
from vyte.utils.git import initialize_repo, create_gitignore

# Initialize git repository
initialize_repo(project_path)

# Create .gitignore file
create_gitignore(project_path, framework="FastAPI")
```

______________________________________________________________________

### vyte.utils.db

Database utilities.

```python
from vyte.utils.db import validate_connection, generate_connection_string

# Validate database connection
is_valid = validate_connection("postgresql://user:pass@localhost/db")

# Generate connection string
conn_str = generate_connection_string(
    dialect="postgresql",
    driver="asyncpg",
    username="user",
    password="pass",
    host="localhost",
    port=5432,
    database="mydb",
)
```

______________________________________________________________________

## CLI Module

### vyte.cli.commands

Command-line interface functions.

```python
from vyte.cli.commands import create_project, list_projects, show_project_info

# Create project programmatically
create_project(
    name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
)

# List projects in directory
projects = list_projects(Path.cwd())

# Show project info
info = show_project_info("my-api")
```

______________________________________________________________________

## Type Definitions

### Common Types

```python
from typing import Literal

# Framework choices
Framework = Literal["FastAPI", "Flask-Restx", "Django-Rest"]

# ORM choices
ORM = Literal["SQLAlchemy", "TortoiseORM", "Peewee"]

# Database choices
Database = Literal["PostgreSQL", "MySQL", "SQLite"]


# Project info
class ProjectInfo(TypedDict):
    name: str
    framework: Framework
    orm: ORM
    database: Database
    python_version: str
    created_at: str
```

______________________________________________________________________

## Exceptions

### Custom Exceptions

```python
class VyteError(Exception):
    """Base exception for Vyte."""

    pass


class ValidationError(VyteError):
    """Configuration validation failed."""

    pass


class GenerationError(VyteError):
    """Error during project generation."""

    pass


class CompatibilityError(VyteError):
    """Incompatible framework/ORM/database combination."""

    pass


class TemplateError(VyteError):
    """Template rendering error."""

    pass
```

______________________________________________________________________

## Constants

### Default Values

```python
# vyte.core.config
DEFAULT_PYTHON_VERSION = "3.11"
SUPPORTED_FRAMEWORKS = ["FastAPI", "Flask-Restx", "Django-Rest"]
SUPPORTED_ORMS = ["SQLAlchemy", "TortoiseORM", "Peewee"]
SUPPORTED_DATABASES = ["PostgreSQL", "MySQL", "SQLite"]

# Compatibility matrix
COMPATIBILITY_MATRIX = {
    "FastAPI": {
        "SQLAlchemy": ["PostgreSQL", "MySQL", "SQLite"],
        "TortoiseORM": ["PostgreSQL", "MySQL", "SQLite"],
        "Peewee": [],
    },
    "Flask-Restx": {
        "SQLAlchemy": ["PostgreSQL", "MySQL", "SQLite"],
        "TortoiseORM": [],
        "Peewee": ["SQLite"],
    },
}
```

______________________________________________________________________

## Examples

### Complete Generation Flow

```python
from pathlib import Path
from vyte.core.config import ProjectConfig
from vyte.core.generator import ProjectGenerator
from vyte.core.dependencies import DependencyManager

# 1. Create configuration
config = ProjectConfig(
    project_name="my-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
    use_alembic=True,
    use_docker=True,
    use_tests=True,
)

# 2. Validate configuration
if not config.validate():
    raise ValueError("Invalid configuration")

# 3. Generate project
generator = ProjectGenerator(
    project_name=config.project_name,
    framework=config.framework,
    orm=config.orm,
    database=config.database,
)

project_path = generator.generate()

# 4. Get dependencies
dep_manager = DependencyManager(config)
deps = dep_manager.get_dependencies()

print(f"Project created at: {project_path}")
print(f"Required packages: {deps['core']}")
```

### Custom Template Rendering

```python
from vyte.core.renderer import TemplateRenderer
from vyte.core.config import ProjectConfig

config = ProjectConfig(
    project_name="custom-api",
    framework="FastAPI",
    orm="SQLAlchemy",
    database="PostgreSQL",
)

renderer = TemplateRenderer(config)

# Custom context
context = {
    "app_title": "Custom API",
    "app_description": "My custom API built with Vyte",
    "enable_cors": True,
    "cors_origins": ["http://localhost:3000"],
}

# Render with custom context
content = renderer.render_template("fastapi/main.py.j2", context)
```

______________________________________________________________________

## Integration Examples

### With FastAPI

```python
# Generated by Vyte - app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app.api.routes import users

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="My API")
app.include_router(users.router)
```

### With Flask-Restx

```python
# Generated by Vyte - app/main.py
from flask import Flask
from flask_restx import Api
from app.database import db
from app.api.routes import users

app = Flask(__name__)
api = Api(app, title="My API")

# Initialize database
db.init_app(app)

# Register namespaces
api.add_namespace(users.api, path="/users")
```

______________________________________________________________________

## Version Information

```python
from vyte import __version__

print(f"Vyte version: {__version__}")
```

______________________________________________________________________

## Next Steps

- [Quick Start](quickstart.md) - Get started with Vyte
- [Configuration](configuration.md) - Configure your projects
- [CLI Reference](cli.md) - Command-line interface
- [GitHub Repository](https://github.com/yourusername/vyte)
