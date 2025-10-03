"""
Strategy for Django-Rest projects
"""
from pathlib import Path
from rdt.strategies.base import BaseStrategy
from rdt.core.renderer import TemplateRegistry


class DjangoRestStrategy(BaseStrategy):
    """Strategy for generating Django-Rest projects"""

    def generate_structure(self, project_path: Path):
        """Create Django-specific directory structure"""
        app_name = self.config.name.replace('-', '_')

        dirs = [
            f'{app_name}',  # Main Django app
            f'{app_name}/api',  # DRF views/serializers
            f'{app_name}/management',
            f'{app_name}/management/commands',
        ]

        for dir_name in dirs:
            (project_path / dir_name).mkdir(parents=True, exist_ok=True)
            (project_path / dir_name / '__init__.py').touch()

    def generate_files(self, project_path: Path):
        """Generate Django-Rest specific files"""
        app_name = self.config.name.replace('-', '_')
        templates = TemplateRegistry.get_templates_for_config(
            self.config.framework,
            self.config.orm,
            self.config.auth_enabled,
            False
        )

        # settings.py
        if 'settings' in templates:
            self.renderer.render_to_file(
                templates['settings'],
                project_path / app_name / 'settings.py',
                self.context
            )

        # urls.py
        if 'urls' in templates:
            self.renderer.render_to_file(
                templates['urls'],
                project_path / app_name / 'urls.py',
                self.context
            )

        # models.py
        if 'models' in templates:
            self.renderer.render_to_file(
                templates['models'],
                project_path / app_name / 'api' / 'models.py',
                self.context
            )

        # serializers.py
        if 'serializers' in templates:
            self.renderer.render_to_file(
                templates['serializers'],
                project_path / app_name / 'api' / 'serializers.py',
                self.context
            )

        # views.py
        view_key = 'views_auth' if self.config.auth_enabled else 'views'
        if view_key in templates:
            self.renderer.render_to_file(
                templates[view_key],
                project_path / app_name / 'api' / 'views.py',
                self.context
            )

        # manage.py
        manage_py_content = '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{app_name}.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
'''.format(app_name=app_name)

        manage_py_path = project_path / 'manage.py'
        manage_py_path.write_text(manage_py_content)
        manage_py_path.chmod(0o755)  # Make executable
        
        # Security (if auth enabled)
        if self.config.auth_enabled:
            self.renderer.render_to_file(
                TemplateRegistry.COMMON_TEMPLATES['security'],
                project_path / app_name / 'security.py',
                self.context
            )
        
        # Generate tests
        if self.config.testing_suite:
            self._generate_tests(project_path)
    
    def _generate_tests(self, project_path: Path):
        """Generate test files specific to Django-Rest"""
        # Obtener templates de tests específicos
        test_templates = TemplateRegistry.TEST_TEMPLATES.get(
            self.config.framework, {}
        ).get(self.config.orm, {})
        
        if not test_templates:
            print(f"Warning: No test templates found for {self.config.framework} + {self.config.orm}")
            return
        
        # tests/conftest.py
        if 'conftest' in test_templates:
            self.renderer.render_to_file(
                test_templates['conftest'],
                project_path / 'tests' / 'conftest.py',
                self.context
            )
        
        # tests/test_api.py
        if 'test_api' in test_templates:
            self.renderer.render_to_file(
                test_templates['test_api'],
                project_path / 'tests' / 'test_api.py',
                self.context
            )
        
        # tests/test_models.py
        if 'test_models' in test_templates:
            self.renderer.render_to_file(
                test_templates['test_models'],
                project_path / 'tests' / 'test_models.py',
                self.context
            )
        
        # tests/test_security.py (común)
        if 'test_security' in test_templates:
            self.renderer.render_to_file(
                test_templates['test_security'],
                project_path / 'tests' / 'test_security.py',
                self.context
            )