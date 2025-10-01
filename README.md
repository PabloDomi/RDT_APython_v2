# 🚀 RDT - Rapid Development Tool

[![PyPI version](https://badge.fury.io/py/rdt-api-generator.svg)](https://badge.fury.io/py/rdt-api-generator)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> Professional API project generator for Python. Create production-ready REST APIs in seconds.

## ✨ Features

- 🎯 **Multiple Frameworks**: Flask-Restx, FastAPI, Django-Rest
- 🗄️ **Multiple ORMs**: SQLAlchemy, TortoiseORM, Pewee, Django ORM
- 💾 **Database Support**: PostgreSQL, MySQL, SQLite
- 🔐 **JWT Authentication**: Secure authentication out of the box
- 🐳 **Docker Ready**: Complete Docker and docker-compose setup
- 🧪 **Testing Suite**: Pytest with coverage reports
- 📚 **Auto Documentation**: Swagger/OpenAPI automatic docs
- ⚡ **Modern Stack**: Python 3.11+, Pydantic v2, async support
- 🎨 **Beautiful CLI**: Rich terminal UI with interactive setup

## 🚀 Quick Start

### Installation

```bash
# Using pip
pip install rdt-api-generator

# Using pipx (recommended)
pipx install rdt-api-generator

# From source
git clone https://github.com/yourusername/rdt.git
cd rdt
pip install -e .
```

### Create Your First Project

```bash
# Interactive mode (recommended)
rdt create

# Or specify options directly
rdt create \
  --name my-api \
  --framework FastAPI \
  --orm SQLAlchemy \
  --database PostgreSQL
```

### What You Get

```
my-api/
├── src/
│   ├── __init__.py          # App factory
│   ├── main.py              # Entry point
│   ├── config/
│   │   └── config.py        # Pydantic settings
│   ├── models/
│   │   └── models.py        # Database models
│   ├── routes/
│   │   └── routes_example.py
│   ├── services/
│   └── security.py          # JWT & security
├── tests/
│   ├── test_api.py
│   ├── test_models.py
│   └── conftest.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md
```

## 📖 Usage

### Interactive Mode

The easiest way to create a project:

```bash
rdt create
```

Follow the prompts to configure your project.

### Command Line Options

```bash
rdt create \
  --name my-api \
  --framework FastAPI \
  --orm SQLAlchemy \
  --database PostgreSQL \
  --auth \
  --docker \
  --tests \
  --git
```

### Available Commands

```bash
# Create new project
rdt create

# Show framework information
rdt info FastAPI

# List all frameworks and ORMs
rdt list

# Show dependencies for configuration
rdt deps FastAPI --orm SQLAlchemy

# Validate existing project
rdt validate ./my-api

# Open documentation
rdt docs

# Show version
rdt --version
```

## 🎯 Supported Combinations

| Framework    | Compatible ORMs                    | Async Support |
|-------------|-----------------------------------|---------------|
| Flask-Restx | SQLAlchemy, Pewee                 | ❌ Sync       |
| FastAPI     | SQLAlchemy (async), TortoiseORM   | ✅ Async      |
| Django-Rest | Django ORM                        | ❌ Sync       |

## 🔧 Configuration

Projects use Pydantic Settings for configuration:

```python
# .env file
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
JWT_SECRET_KEY=your-secret-key-here
ENVIRONMENT=development
DEBUG=True
```

## 🧪 Testing

Generated projects include complete testing setup:

```bash
# Run tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Open coverage report
open htmlcov/index.html
```

## 🐳 Docker Support

Run your project with Docker:

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

## 📚 Documentation

- [Full Documentation](https://rdt.readthedocs.io)
- [API Reference](https://rdt.readthedocs.io/api)
- [Examples](./examples)
- [Contributing Guide](./CONTRIBUTING.md)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

```bash
# Clone repo
git clone https://github.com/yourusername/rdt.git
cd rdt

# Install with dev dependencies
poetry install

# Run tests
pytest

# Format code
black .
ruff check .
```

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Click](https://click.palletsprojects.com/)
- UI powered by [Rich](https://rich.readthedocs.io/)
- Templates with [Jinja2](https://jinja.palletsprojects.com/)
- Validation with [Pydantic](https://docs.pydantic.dev/)

## 📧 Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/rdt/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/rdt/discussions)
- **Email**: your.email@example.com

---

Made with ❤️ by the RDT team