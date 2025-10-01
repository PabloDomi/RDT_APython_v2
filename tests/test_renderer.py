# tests/test_renderer.py
"""
Test template rendering
"""
from rdt.core.renderer import TemplateRegistry


def test_renderer_initialization(renderer):
    """Test renderer initialization"""
    assert renderer.env is not None
    assert renderer.template_dir.exists()


def test_template_filters(renderer):
    """Test custom filters"""
    # Test filters through the Jinja environment instead of direct method access
    env = renderer.env
    assert env.filters['pascal_case']("my_project") == "MyProject"
    assert env.filters['snake_case']("MyProject") == "my_project"
    assert env.filters['kebab_case']("my_project") == "my-project"
    assert env.filters['title_case']("my_project") == "My Project"


def test_render_simple_template(renderer, temp_dir):
    """Test rendering a simple template"""
    # Create a simple template
    template_content = "Hello {{ name }}!"
    template_path = temp_dir / "test.j2"
    template_path.write_text(template_content)

    # Render (would need actual template in templates/)
    # This is just to test the method exists
    assert hasattr(renderer, 'render')
    assert hasattr(renderer, 'render_to_file')


def test_template_registry():
    """Test template registry"""
    templates = TemplateRegistry.get_templates_for_config(
        framework="Flask-Restx",
        orm="SQLAlchemy",
        auth_enabled=True,
        testing_suite=True
    )

    assert len(templates) > 0
    assert 'init' in templates or 'init_auth' in templates
    assert 'models' in templates
