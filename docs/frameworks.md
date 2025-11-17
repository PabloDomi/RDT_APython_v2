# Frameworks

Vyte supports multiple modern Python web frameworks. Each has its own strengths and is suitable for different use cases.

## Supported Frameworks

### FastAPI

<div class="admonition tip">
<p class="admonition-title">Recommended for new projects</p>
<p>FastAPI is the recommended choice for most new projects due to its modern design, excellent performance, and automatic documentation.</p>
</div>

**Type**: Modern async web framework
**Version**: 0.104+
**Async Support**: Yes
**Documentation**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)

#### Key Features

- ⚡ **High Performance** - One of the fastest Python frameworks (on par with NodeJS and Go)
- 📚 **Automatic Docs** - Interactive API documentation (Swagger UI and ReDoc)
- 🎯 **Type Hints** - Full type hints and validation with Pydantic v2
- ⚡ **Async/Await** - Native async support for high concurrency
- 💉 **Dependency Injection** - Clean and powerful DI system
- 🔒 **Security** - Built-in security utilities (OAuth2, JWT, etc.)

#### Best For

- Microservices
- High-performance APIs
- Real-time applications
- Modern async applications
- Projects requiring auto-generated docs

#### Compatible ORMs

- ✅ SQLAlchemy (async)
- ✅ TortoiseORM (async)

#### Example Usage

```python
from fastapi import FastAPI

app = FastAPI(title="My API")


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

______________________________________________________________________

### Flask-Restx

**Type**: Extension of Flask for REST APIs
**Version**: 1.2+
**Async Support**: No (sync only)
**Documentation**: [flask-restx.readthedocs.io](https://flask-restx.readthedocs.io/)

#### Key Features

- 🏗️ **Battle-Tested** - Built on top of mature Flask framework
- 📚 **Swagger Integration** - Built-in Swagger UI
- 🔧 **Flexible** - Highly customizable and extensible
- 📦 **Rich Ecosystem** - Access to entire Flask ecosystem
- 🎯 **Request Parsing** - Built-in request parsing and validation
- 📝 **API Namespaces** - Organize endpoints with namespaces

#### Best For

- Traditional web applications
- When async is not needed
- Projects with Flask experience
- Gradual migration from Flask
- When you need Flask extensions

#### Compatible ORMs

- ✅ SQLAlchemy (sync)
- ✅ Peewee (sync)

#### Example Usage

```python
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, title="My API")


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello World"}
```

______________________________________________________________________

### Django-Rest

<div class="admonition warning">
<p class="admonition-title">Coming Soon</p>
<p>Django Rest Framework support is planned for a future release.</p>
</div>

**Type**: Powerful toolkit for building Web APIs on Django
**Version**: 3.14+
**Async Support**: Partial (Django 4.1+)
**Documentation**: [django-rest-framework.org](https://www.django-rest-framework.org/)

#### Planned Features

- 🏢 **Enterprise Ready** - Production-ready out of the box
- 📚 **Browsable API** - Web-browsable API interface
- 🔐 **Authentication** - Multiple authentication schemes
- 🎯 **Serializers** - Powerful serialization system
- 📝 **ViewSets** - Quick CRUD operations
- 🔒 **Permissions** - Flexible permission system

______________________________________________________________________

## Comparison Matrix

| Feature        | FastAPI     | Flask-Restx | Django-Rest      |
| -------------- | ----------- | ----------- | ---------------- |
| Performance    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐      | ⭐⭐⭐           |
| Learning Curve | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐           |
| Async Support  | ✅ Native   | ❌ No       | 🟡 Partial       |
| Auto Docs      | ✅ Built-in | ✅ Swagger  | ✅ Browsable API |
| Type Safety    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐      | ⭐⭐⭐           |
| Ecosystem      | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐       |
| Maturity       | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐       |

## Choosing a Framework

### Choose FastAPI if you want:

- Maximum performance
- Modern async/await patterns
- Automatic interactive documentation
- Full type safety with Pydantic
- Microservices or API-only applications

### Choose Flask-Restx if you want:

- Battle-tested stability
- Simple synchronous code
- Flask ecosystem compatibility
- Gradual migration from existing Flask apps
- Traditional request-response pattern

### Choose Django-Rest if you want:

- Full-featured framework with admin panel
- ORM with migrations built-in
- Enterprise-grade authentication
- Extensive third-party packages
- Monolithic application structure

## Next Steps

- [ORMs & Databases](databases.md) - Learn about supported ORMs
- [CLI Commands](cli.md) - See how to generate projects
- [Quick Start](quickstart.md) - Create your first project
