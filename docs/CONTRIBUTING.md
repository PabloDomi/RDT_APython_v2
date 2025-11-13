# Contributing to Vyte

Thank you for your interest in contributing to Vyte! This document provides guidelines and instructions for contributing.

## 🎯 Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Git
- pip

### Setting Up Development Environment

1. **Fork and Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/Vyte.git
cd vyte
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

4. **Verify Installation**

```bash
python -m pytest
```

## 📝 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Test additions/changes

### 2. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Keep functions focused and small

### 3. Write Tests

- Add tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=vyte --cov-report=html

# Run specific test file
pytest tests/test_cli.py
```

### 4. Format and Lint

```bash
# Format code with black
black .

# Lint with ruff
ruff check .

# Type check with mypy (if configured)
mypy vyte
```

### 5. Commit Your Changes

Use clear, descriptive commit messages:

```bash
git add .
git commit -m "feat: add support for MongoDB with MongoEngine"
```

Commit message format:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Test additions/changes
- `chore:` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:

- Clear title and description
- Reference to related issues
- Screenshots (if applicable)
- Testing details

## 🧪 Testing Guidelines

### Test Structure

```python
def test_feature_name():
    """
    Test description explaining what is being tested
    """
    # Arrange
    setup_code()

    # Act
    result = function_to_test()

    # Assert
    assert result == expected_value
```

### Test Coverage

- Unit tests for individual functions
- Integration tests for component interactions
- End-to-end tests for complete workflows

### Running Tests

```bash
# All tests
pytest

# Specific test file
pytest tests/test_cli.py

# Specific test function
pytest tests/test_cli.py::test_cli_help

# With verbose output
pytest -v

# Stop on first failure
pytest -x

# Run only integration tests
pytest -m integration

# Skip integration tests
pytest -m "not integration"
```

## 📚 Documentation

### Code Documentation

- Add docstrings to all public functions and classes
- Follow Google or NumPy docstring format
- Include examples in docstrings when helpful

Example:

```python
def create_project(config: ProjectConfig) -> Path:
    """
    Create a new project from configuration.

    Args:
        config: Project configuration containing name, framework, etc.

    Returns:
        Path to the created project directory.

    Raises:
        ValueError: If configuration is invalid.
        FileExistsError: If project directory already exists.

    Example:
        >>> config = ProjectConfig(name="my-api", framework="FastAPI")
        >>> path = create_project(config)
        >>> print(path)
        /path/to/my-api
    """
    pass
```

### Documentation Files

When updating documentation:

- Update relevant `.md` files in `docs/`
- Update `README.md` if needed
- Keep examples up-to-date

## 🐛 Reporting Bugs

### Before Reporting

1. Check existing issues
1. Verify you're using the latest version
1. Try to reproduce with minimal example

### Bug Report Template

```markdown
**Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Run command '...'
2. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python Version: [e.g., 3.11.5]
- Vyte Version: [e.g., 2.0.4]

**Additional Context**
Any other relevant information
```

## ✨ Feature Requests

We welcome feature suggestions! Please provide:

1. **Use Case**: Why is this feature needed?
1. **Description**: What should the feature do?
1. **Examples**: How would users interact with it?
1. **Alternatives**: What alternatives have you considered?

## 🎨 Code Style

### Python Style

- Follow PEP 8
- Use type hints
- Maximum line length: 100 characters
- Use meaningful variable names

```python
# Good
def generate_project(config: ProjectConfig) -> Path:
    project_path = Path(config.name)
    return project_path


# Avoid
def gen(c):
    p = Path(c.name)
    return p
```

### Imports

Organize imports in this order:

1. Standard library
1. Third-party packages
1. Local imports

```python
import sys
from pathlib import Path

import click
from rich.console import Console

from ..core.config import ProjectConfig
from .display import show_welcome
```

## 🔍 Code Review Process

### What We Look For

- Code quality and clarity
- Test coverage
- Documentation
- Performance considerations
- Security implications
- Breaking changes

### Review Timeline

- Initial review: Within 3-5 days
- Follow-up reviews: Within 2 days
- Approval requires: 1 maintainer approval

## 📦 Release Process

### Version Numbering

We follow Semantic Versioning (SemVer):

- `MAJOR.MINOR.PATCH`
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

### Release Checklist

1. Update version in `vyte/__version__.py`
1. Update `CHANGELOG.md`
1. Run full test suite
1. Update documentation
1. Create release tag
1. Publish to PyPI

## 🤝 Community

### Getting Help

- GitHub Issues: Bug reports and features
- Discussions: Questions and community chat
- Email: Domi@usal.es

### Recognition

Contributors are recognized in:

- Release notes
- `CONTRIBUTORS.md` file
- GitHub contributors page

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

______________________________________________________________________

Thank you for contributing to Vyte! 🚀

Your efforts help make Python API development faster and easier for everyone.
