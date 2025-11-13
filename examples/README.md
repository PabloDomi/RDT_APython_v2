# Vyte Examples

This directory contains example projects generated with Vyte to demonstrate different configurations and use cases.

## 📁 Example Projects

### Basic Examples

1. **fastapi-sqlalchemy-postgres/**

   - FastAPI with SQLAlchemy ORM
   - PostgreSQL database
   - JWT authentication
   - Full async support
   - Docker ready

1. **flask-restx-sqlalchemy-sqlite/**

   - Flask-RESTX with SQLAlchemy ORM
   - SQLite database (easy local development)
   - JWT authentication
   - Swagger documentation

1. **fastapi-tortoise-postgres/**

   - FastAPI with TortoiseORM
   - PostgreSQL database
   - Async ORM operations
   - Aerich migrations

### Advanced Examples

4. **microservices/**

   - Multiple Vyte projects working together
   - Inter-service communication
   - Shared authentication
   - Docker Compose orchestration

1. **production-ready/**

   - Production deployment configuration
   - Environment-based settings
   - Logging and monitoring
   - Health checks
   - Rate limiting

## 🚀 How to Use Examples

### Generate an Example Project

You can recreate any example using Vyte:

```bash
# FastAPI + SQLAlchemy + PostgreSQL
vyte create \
  --name my-fastapi-app \
  --framework FastAPI \
  --orm SQLAlchemy \
  --database PostgreSQL \
  --auth \
  --docker \
  --tests \
  --git

# Flask-RESTX + SQLAlchemy + SQLite
vyte create \
  --name my-flask-app \
  --framework Flask-Restx \
  --orm SQLAlchemy \
  --database SQLite \
  --auth \
  --docker \
  --tests \
  --git
```

### Run an Example

Each example includes its own README with specific instructions, but generally:

```bash
# Navigate to example
cd examples/fastapi-sqlalchemy-postgres

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your settings

# Run database migrations (if applicable)
alembic upgrade head

# Start the application
uvicorn src.main:app --reload

# Or use Docker
docker-compose up -d
```

## 📚 Example Descriptions

### fastapi-sqlalchemy-postgres

A modern async API with:

- User authentication with JWT
- CRUD operations for items/resources
- Database migrations with Alembic
- Pydantic models for validation
- Async SQLAlchemy queries
- Comprehensive tests
- API documentation at `/docs`

**Best for**: Production-ready async APIs, microservices

### flask-restx-sqlalchemy-sqlite

A classic REST API with:

- Synchronous operations
- Swagger UI integration
- SQLAlchemy ORM
- SQLite for easy setup
- Namespace organization
- Request/response models

**Best for**: Learning, rapid prototyping, internal tools

### fastapi-tortoise-postgres

A fully async stack with:

- TortoiseORM for async operations
- Aerich for migrations
- Pydantic integration
- PostgreSQL async driver
- Native async/await

**Best for**: High-performance async applications

## 🎯 Learning Path

Recommended order for exploring examples:

1. **Start here**: `flask-restx-sqlalchemy-sqlite`

   - Simplest setup
   - Easy to understand
   - No external dependencies

1. **Next**: `fastapi-sqlalchemy-postgres`

   - Modern async patterns
   - Production-like setup
   - Docker integration

1. **Advanced**: `fastapi-tortoise-postgres`

   - Fully async ORM
   - Advanced patterns
   - Performance optimization

1. **Expert**: `microservices/`

   - Multi-service architecture
   - Service communication
   - Deployment strategies

## 🔧 Customization Examples

Each example can be customized to show:

### Adding Custom Endpoints

```python
# In src/routes/custom.py
from fastapi import APIRouter

router = APIRouter(prefix="/custom", tags=["custom"])


@router.get("/hello")
async def hello():
    return {"message": "Hello from custom endpoint!"}
```

### Adding Middleware

```python
# In src/main.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Custom Models

```python
# In src/models/models.py
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
```

## 🐳 Docker Examples

All examples include Docker support:

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

## 🧪 Testing Examples

Run tests for any example:

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_api.py -v
```

## 📖 Additional Resources

- [Vyte Documentation](../docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Flask-RESTX Documentation](https://flask-restx.readthedocs.io/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## 🤝 Contributing Examples

Have a great example to share? We'd love to include it!

1. Generate your project with Vyte
1. Add a comprehensive README
1. Include tests
1. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

## 💡 Tips

- Start with SQLite for local development
- Use PostgreSQL for production
- Enable `--no-docker` if you don't need containers
- Add `--no-auth` for public APIs
- Always include tests (`--tests`)

## 🆘 Getting Help

If you have questions about the examples:

1. Check the example's README
1. Review the main documentation
1. Open a discussion on GitHub
1. Report issues if you find bugs

______________________________________________________________________

Happy coding with Vyte! 🚀
