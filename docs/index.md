# Welcome to Vyte

<p align="center">
  <img src="../images/Logo_V_Transparente.png" alt="Vyte Logo" width="400"/>
</p>

<p align="center">
  <strong>Professional API project generator for Python. Create production-ready REST APIs in seconds.</strong>
</p>

______________________________________________________________________

## What is Vyte?

Vyte is a powerful command-line tool that generates professional, production-ready REST API projects for Python. It's like Vite for JavaScript, but for Python APIs.

### Key Features

✨ **Multiple Frameworks**

- Flask-Restx
- FastAPI
- Django-Rest (coming soon)

🗄️ **Multiple ORMs**

- SQLAlchemy
- TortoiseORM
- Peewee
- Django ORM (coming soon)

💾 **Database Support**

- PostgreSQL
- MySQL
- SQLite

🔐 **Security First**

- JWT authentication out of the box
- Secure password hashing
- CORS configuration

🐳 **DevOps Ready**

- Complete Docker setup
- docker-compose configuration
- Production-ready Dockerfile

🧪 **Testing Built-in**

- Pytest configuration
- Coverage reports
- Example tests included

📚 **Auto Documentation**

- Swagger/OpenAPI automatic docs
- Interactive API explorer
- Auto-generated from code

⚡ **Modern Stack**

- Python 3.11+
- Pydantic v2
- Async support
- Type hints everywhere

🎨 **Beautiful CLI**

- Rich terminal UI
- Interactive setup wizard
- Clear, helpful messages

## Quick Example

```bash
# Install
pip install vyte

# Create a new API project
vyte create

# Follow the interactive prompts or use flags:
vyte create \
  --name my-api \
  --framework FastAPI \
  --orm SQLAlchemy \
  --database PostgreSQL \
  --auth \
  --docker
```

## Philosophy

Vyte follows these principles:

1. **Convention over Configuration**: Sensible defaults that just work
1. **Best Practices**: Generated code follows Python and framework best practices
1. **Production Ready**: Not just prototypes, but deployable applications
1. **Developer Experience**: Beautiful CLI, clear documentation, helpful errors
1. **Modern Stack**: Latest stable versions of frameworks and libraries

## Use Cases

### 🚀 Rapid Prototyping

Quickly spin up a new API to test an idea or build a proof of concept.

### 🏢 Microservices

Generate multiple services with consistent structure and standards.

### 📚 Learning

Perfect for learning modern Python API development with real-world patterns.

### 🎯 Startups

Get from zero to deployed faster with production-ready boilerplate.

## Next Steps

- [**Quick Start**](quickstart.md) - Get started in 5 minutes
- [**CLI Commands**](cli.md) - Learn all available commands
- [**Configuration**](configuration.md) - Customize your projects
- [**Integration**](integration.md) - Connect with your tools

## Community

- [GitHub Issues](https://github.com/PabloDomi/Vyte/issues) - Report bugs or request features
- [Discussions](https://github.com/PabloDomi/Vyte/discussions) - Ask questions and share ideas
- [Contributing](CONTRIBUTING.md) - Help make Vyte better

## License

Vyte is open source software licensed under the [MIT License](../LICENSE).
