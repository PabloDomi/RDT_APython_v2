# Configuration Guide

Learn how to configure your Vyte-generated projects for different environments and use cases.

## Environment Variables

All Vyte projects use environment variables for configuration. This follows the [12-factor app](https://12factor.net/) methodology.

### Configuration Files

Your project includes:

- **`.env.example`** - Template with all available variables
- **`.env`** - Your actual configuration (create from example, not in git)
- **`config.py`** (optional) - Type-safe configuration loader

### Creating Your Configuration

```bash
# Copy the example file
cp .env.example .env

# Edit with your settings
nano .env  # or your preferred editor
```

______________________________________________________________________

## Core Settings

### Database Configuration

#### DATABASE_URL

The most important setting - your database connection string.

**Format**: `dialect+driver://username:password@host:port/database`

```ini
# PostgreSQL (Production)
DATABASE_URL=postgresql://myuser:mypass@localhost:5432/mydb

# PostgreSQL (Async - FastAPI)
DATABASE_URL=postgresql+asyncpg://myuser:mypass@localhost:5432/mydb

# MySQL
DATABASE_URL=mysql://myuser:mypass@localhost:3306/mydb

# SQLite (Development)
DATABASE_URL=sqlite:///./database.db

# SQLite (Async)
DATABASE_URL=sqlite+aiosqlite:///./database.db
```

<div class="admonition warning">
<p class="admonition-title">Security Warning</p>
<p>Never commit your <code>.env</code> file! Keep credentials secure and use environment-specific values.</p>
</div>

#### Additional Database Settings

```ini
# Connection pool settings (SQLAlchemy)
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=3600

# Echo SQL queries (development only!)
DB_ECHO=false
```

______________________________________________________________________

### Application Settings

```ini
# Application
APP_NAME=My API
APP_VERSION=1.0.0
APP_DESCRIPTION=My amazing API

# Server
HOST=0.0.0.0
PORT=8000

# Environment
ENVIRONMENT=development  # development, staging, production

# Debug mode (NEVER use in production!)
DEBUG=true
```

______________________________________________________________________

### Security Settings

```ini
# Secret key for JWT, sessions, etc.
SECRET_KEY=your-super-secret-key-change-this-in-production

# JWT Settings
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
JWT_REFRESH_EXPIRE_DAYS=7

# CORS Settings
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8080"]
CORS_CREDENTIALS=true
CORS_METHODS=["*"]
CORS_HEADERS=["*"]

# API Keys
API_KEY_HEADER=X-API-Key
```

<div class="admonition danger">
<p class="admonition-title">Critical</p>
<p>Always generate a strong random <code>SECRET_KEY</code> for production!</p>
</div>

#### Generate a Secure Secret Key

```python
import secrets

print(secrets.token_urlsafe(32))
```

______________________________________________________________________

### Logging Configuration

```ini
# Logging
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FORMAT=json  # json or text
LOG_FILE=logs/app.log
LOG_ROTATION=1 day
LOG_RETENTION=30 days
```

______________________________________________________________________

## Framework-Specific Configuration

### FastAPI

```ini
# FastAPI specific
FASTAPI_TITLE=My API
FASTAPI_DESCRIPTION=API built with Vyte
FASTAPI_VERSION=1.0.0
FASTAPI_OPENAPI_URL=/openapi.json
FASTAPI_DOCS_URL=/docs
FASTAPI_REDOC_URL=/redoc

# Disable docs in production
FASTAPI_DOCS_ENABLED=true
```

### Flask-Restx

```ini
# Flask specific
FLASK_APP=app.main
FLASK_ENV=development  # development or production
FLASK_DEBUG=true

# Flask-Restx
RESTX_MASK_SWAGGER=false
RESTX_VALIDATE=true
SWAGGER_UI_DOC_EXPANSION=list
```

______________________________________________________________________

## ORM-Specific Configuration

### SQLAlchemy

```ini
# SQLAlchemy
SQLALCHEMY_DATABASE_URI=${DATABASE_URL}
SQLALCHEMY_ECHO=false
SQLALCHEMY_TRACK_MODIFICATIONS=false
SQLALCHEMY_POOL_SIZE=5
SQLALCHEMY_MAX_OVERFLOW=10
```

### TortoiseORM

```ini
# Tortoise ORM
TORTOISE_DB_URL=${DATABASE_URL}
TORTOISE_GENERATE_SCHEMAS=true
TORTOISE_ADD_EXCEPTION_HANDLERS=true
```

### Peewee

```ini
# Peewee
PEEWEE_DATABASE_URL=${DATABASE_URL}
PEEWEE_MAX_CONNECTIONS=20
```

______________________________________________________________________

## Environment-Based Configuration

### Development Environment

```ini
# .env.development
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
DB_ECHO=true
DATABASE_URL=sqlite:///./dev.db

# Enable all docs
FASTAPI_DOCS_ENABLED=true
```

### Staging Environment

```ini
# .env.staging
ENVIRONMENT=staging
DEBUG=false
LOG_LEVEL=INFO
DATABASE_URL=postgresql://user:pass@staging-db:5432/myapp

# Docs enabled but protected
FASTAPI_DOCS_ENABLED=true
```

### Production Environment

```ini
# .env.production
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=WARNING
DATABASE_URL=postgresql://user:pass@prod-db:5432/myapp

# Disable docs in production
FASTAPI_DOCS_ENABLED=false
DB_ECHO=false

# Strict security
CORS_ORIGINS=["https://myapp.com"]
```

### Loading Environment-Specific Config

```bash
# Development
cp .env.development .env

# Production
cp .env.production .env
```

Or use direnv for automatic switching:

```bash
# Install direnv
brew install direnv  # macOS
apt install direnv   # Ubuntu

# Create .envrc
echo "dotenv .env.development" > .envrc
direnv allow
```

______________________________________________________________________

## Configuration Management

### Using python-dotenv

Vyte projects use python-dotenv to load environment variables:

```python
# app/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Database
    database_url: str
    db_echo: bool = False

    # Application
    app_name: str = "My API"
    debug: bool = False

    # Security
    secret_key: str
    jwt_algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings():
    return Settings()
```

### Using the Configuration

```python
from app.config import get_settings

settings = get_settings()

# Access settings
print(settings.database_url)
print(settings.app_name)
```

______________________________________________________________________

## Database Connection Examples

### PostgreSQL with Connection Pool

```python
# app/database.py (SQLAlchemy)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    pool_size=settings.db_pool_size,
    max_overflow=settings.db_max_overflow,
    pool_timeout=settings.db_pool_timeout,
    pool_recycle=settings.db_pool_recycle,
    echo=settings.db_echo,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### PostgreSQL Async (FastAPI)

```python
# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

engine = create_async_engine(
    settings.database_url,
    echo=settings.db_echo,
    future=True,
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with async_session() as session:
        yield session
```

______________________________________________________________________

## CORS Configuration

### FastAPI CORS

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings

settings = get_settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)
```

### Flask CORS

```python
# app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.config import get_settings


def create_app():
    app = Flask(__name__)
    settings = get_settings()

    CORS(
        app,
        origins=settings.cors_origins,
        supports_credentials=settings.cors_credentials,
    )

    return app
```

______________________________________________________________________

## Alembic Configuration

### alembic.ini

```ini
[alembic]
script_location = alembic
file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s

# Get database URL from environment
sqlalchemy.url =
```

### alembic/env.py

```python
from app.database import Base
from app.config import get_settings

settings = get_settings()
config.set_main_option("sqlalchemy.url", settings.database_url)

# Import all models for autogenerate
from app.models import *

target_metadata = Base.metadata
```

______________________________________________________________________

## Docker Configuration

### Using Environment Variables in Docker

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/myapp
      - SECRET_KEY=${SECRET_KEY}
      - DEBUG=false
    env_file:
      - .env.production

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=myapp
```

______________________________________________________________________

## Configuration Checklist

### Development Setup

- ✅ Copy `.env.example` to `.env`
- ✅ Set `DATABASE_URL` for local database
- ✅ Set `DEBUG=true`
- ✅ Set `LOG_LEVEL=DEBUG`
- ✅ Generate a `SECRET_KEY` (any string is fine for dev)

### Production Setup

- ✅ Use strong random `SECRET_KEY`
- ✅ Set `DEBUG=false`
- ✅ Use production database URL
- ✅ Set `ENVIRONMENT=production`
- ✅ Configure proper `CORS_ORIGINS`
- ✅ Set `LOG_LEVEL=WARNING` or `ERROR`
- ✅ Disable API documentation if needed
- ✅ Enable SSL/TLS for database connections
- ✅ Use environment variables from secure vault

______________________________________________________________________

## Best Practices

### 1. Never Commit Secrets

```gitignore
# .gitignore
.env
.env.local
.env.*.local
*.key
*.pem
```

### 2. Use Different Configs per Environment

```
.env.development
.env.staging
.env.production
```

### 3. Validate Configuration on Startup

```python
# app/main.py
from app.config import get_settings

settings = get_settings()

# Fail fast if required settings are missing
assert settings.secret_key, "SECRET_KEY must be set"
assert settings.database_url, "DATABASE_URL must be set"
```

### 4. Use Type-Safe Settings

Use Pydantic `BaseSettings` for automatic validation and type checking.

### 5. Document Your Variables

Keep `.env.example` up to date with all required variables and comments.

______________________________________________________________________

## Troubleshooting

### Configuration Not Loading

**Problem**: Environment variables not being read

**Solution**:

```python
# Verify .env file location
import os

print(os.getcwd())  # Should be project root

# Test manual load
from dotenv import load_dotenv

load_dotenv(verbose=True)
```

### Database Connection Fails

**Problem**: Can't connect to database

**Solution**:

1. Check DATABASE_URL format
1. Verify database server is running
1. Test connection:
   ```python
   from sqlalchemy import create_engine

   engine = create_engine("your-database-url")
   engine.connect()
   ```

### CORS Errors

**Problem**: Browser blocks requests

**Solution**:

1. Add frontend URL to `CORS_ORIGINS`
1. Set `CORS_CREDENTIALS=true` if using cookies
1. Check browser console for exact error

______________________________________________________________________

## Next Steps

- [Quick Start](quickstart.md) - Create your first project
- [Databases](databases.md) - Learn about ORMs and databases
- [Frameworks](frameworks.md) - Framework-specific guides
- [CLI Reference](cli.md) - Complete command documentation
