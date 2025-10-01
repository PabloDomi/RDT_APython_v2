"""
Strategy for FastAPI projects
"""
from pathlib import Path
from rdt.strategies.base import BaseStrategy
from rdt.core.renderer import TemplateRegistry


class FastAPIStrategy(BaseStrategy):
    """Strategy for generating FastAPI projects"""

    def generate_structure(self, project_path: Path):
        """Create FastAPI-specific directory structure"""
        # Crear src/ primero con su __init__.py
        src_dir = project_path / 'src'
        src_dir.mkdir(exist_ok=True)
        (src_dir / '__init__.py').touch()

        # Crear subdirectorios
        dirs = [
            'src/api',
            'src/schemas',
            'src/crud',
            'alembic',
        ]

        for dir_name in dirs:
            (project_path / dir_name).mkdir(parents=True, exist_ok=True)
            if dir_name.startswith('src/'):
                (project_path / dir_name / '__init__.py').touch()

    def generate_files(self, project_path: Path):
        """Generate FastAPI specific files"""
        templates = TemplateRegistry.get_templates_for_config(
            self.config.framework,
            self.config.orm,
            self.config.auth_enabled,
            False
        )

        # src/main.py (FastAPI app)
        main_key = 'main_auth' if self.config.auth_enabled else 'main'
        if main_key in templates:
            self.renderer.render_to_file(
                templates[main_key],
                project_path / 'src' / 'main.py',
                self.context
            )

        # src/database.py or equivalent (for SQLAlchemy)
        if 'database' in templates:
            self.renderer.render_to_file(
                templates['database'],
                project_path / 'src' / 'database.py',
                self.context
            )

        # src/config/config.py
        if 'config' in templates:
            self.renderer.render_to_file(
                templates['config'],
                project_path / 'src' / 'config' / 'config.py',
                self.context
            )

        # src/models/models.py
        if 'models' in templates:
            self.renderer.render_to_file(
                templates['models'],
                project_path / 'src' / 'models' / 'models.py',
                self.context
            )

        # src/routes/routes_example.py
        route_key = 'routes_auth' if self.config.auth_enabled else 'routes'
        if route_key in templates:
            self.renderer.render_to_file(
                templates[route_key],
                project_path / 'src' / 'api' / 'routes_example.py',
                self.context
            )