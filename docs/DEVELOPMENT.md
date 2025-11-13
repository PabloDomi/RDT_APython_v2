# Development Setup Guide

This guide helps you set up your development environment for contributing to Vyte.

## Prerequisites

- Python 3.11 or higher
- Git
- pip

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PabloDomi/Vyte.git
cd vyte
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n vyte python=3.11
conda activate vyte
```

### 3. Install Dependencies

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install additional dev tools
pip install black ruff isort mypy bandit safety pre-commit
```

### 4. Install Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run code quality checks before each commit.

## Development Workflow

### Making Changes

1. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes

1. Format your code:

```bash
make format
# or manually:
black vyte/ tests/
isort vyte/ tests/
```

4. Run linters:

```bash
make lint
# or manually:
black --check vyte/ tests/
ruff check vyte/ tests/
```

5. Run tests:

```bash
make test
# or with coverage:
make test-cov
```

6. Commit your changes:

```bash
git add .
git commit -m "feat: your descriptive commit message"
```

Pre-commit hooks will automatically run and may modify files. If files are modified, add them and commit again.

### Available Make Commands

```bash
make help              # Show all available commands
make test              # Run tests
make test-cov          # Run tests with coverage
make format            # Format code
make lint              # Check code quality
make security          # Run security scans
make clean             # Clean build artifacts
```

## Code Quality Tools

### Black - Code Formatting

Formats Python code to maintain consistent style:

```bash
black vyte/ tests/
```

### Ruff - Fast Linter

Checks and fixes common Python issues:

```bash
ruff check vyte/ tests/
ruff check --fix vyte/ tests/  # Auto-fix issues
```

### isort - Import Sorting

Organizes imports:

```bash
isort vyte/ tests/
```

### MyPy - Type Checking

Static type checking:

```bash
mypy vyte/ --ignore-missing-imports
```

### Bandit - Security Linting

Finds common security issues:

```bash
bandit -c pyproject.toml -r vyte/
```

## Pre-commit Hooks

Pre-commit hooks run automatically before each commit. You can also run them manually:

```bash
# Run all hooks
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
pre-commit run ruff --all-files
```

### Skipping Pre-commit (Not Recommended)

If you need to commit without running hooks:

```bash
git commit --no-verify -m "your message"
```

## Testing

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=vyte --cov-report=html
```

### Run Specific Tests

```bash
# Single test file
pytest tests/test_cli.py

# Single test function
pytest tests/test_cli.py::test_cli_help

# Integration tests only
pytest -m integration

# Skip integration tests
pytest -m "not integration"
```

### View Coverage Report

```bash
# Generate HTML report
pytest --cov=vyte --cov-report=html

# Open in browser (Linux/Mac)
open htmlcov/index.html

# Windows
start htmlcov/index.html
```

## Configuration Files

- **pyproject.toml**: Project metadata, dependencies, and tool configs
- **.pre-commit-config.yaml**: Pre-commit hooks configuration
- **.editorconfig**: Editor settings for consistent coding style
- **.pylintrc**: Pylint configuration (optional)
- **Makefile**: Common development commands

## Troubleshooting

### Pre-commit Issues

If pre-commit fails:

1. Update pre-commit:

```bash
pre-commit autoupdate
```

2. Clean pre-commit cache:

```bash
pre-commit clean
pre-commit install --install-hooks
```

### Test Failures

1. Clear pytest cache:

```bash
pytest --cache-clear
```

2. Reinstall package:

```bash
pip install -e ".[dev]" --force-reinstall
```

### Import Errors

Make sure you installed the package in editable mode:

```bash
pip install -e .
```

## VS Code Setup (Optional)

Create `.vscode/settings.json`:

```json
{
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.testing.pytestEnabled": true,
    "editor.formatOnSave": true,
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    }
}
```

## PyCharm Setup (Optional)

1. Go to Settings → Tools → External Tools
1. Add Black, Ruff, etc. as external tools
1. Configure File Watchers for automatic formatting

## Next Steps

- Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Check [README.md](README.md) for project documentation
- Browse [docs/](docs/) for detailed documentation

## Getting Help

- GitHub Issues: https://github.com/PabloDomi/Vyte/issues
- Discussions: https://github.com/PabloDomi/Vyte/discussions
- Email: Domi@usal.es

Happy coding! 🚀
