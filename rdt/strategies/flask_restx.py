"""
Strategy for Flask-Restx projects
"""
from pathlib import Path
from rdt.strategies.base import BaseStrategy
from rdt.core.renderer import TemplateRegistry


class FlaskRestxStrategy(BaseStrategy):
    """Strategy for generating Flask-Restx projects"""

    def generate_structure(self, project_path: Path):
        """Create Flask-specific directory structure"""
        dirs = [
            'src/controllers',
            'migrations',  # For Flask-Migrate
        ]

        for dir_name in dirs:
            (project_path / dir_name).mkdir(parents=True, exist_ok=True)
            if dir_name.startswith('src/'):
                (project_path / dir_name / '__init__.py').touch()

    def generate_files(self, project_path: Path):
        """Generate Flask-Restx specific files"""
        templates = TemplateRegistry.get_templates_for_config(
            self.config.framework,
            self.config.orm,
            self.config.auth_enabled,
            False  # Tests handled separately
        )

        # src/__init__.py (app factory)
        init_key = 'init_auth' if self.config.auth_enabled else 'init'
        if init_key in templates:
            self.renderer.render_to_file(
                templates[init_key],
                project_path / 'src' / '__init__.py',
                self.context
            )

        # src/extensions.py
        ext_key = 'extensions_auth' if self.config.auth_enabled else 'extensions'
        if ext_key in templates:
            self.renderer.render_to_file(
                templates[ext_key],
                project_path / 'src' / 'extensions.py',
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
                project_path / 'src' / 'routes' / 'routes_example.py',
                self.context
            )

        # app.py (entry point)
        self.renderer.render_to_file(
            TemplateRegistry.COMMON_TEMPLATES['app'],
            project_path / 'app.py',
            self.context
        )