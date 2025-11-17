# Quick Start Guide

Get started with Vyte in minutes! This guide will walk you through installing Vyte, creating your first project, and running it.

## Installation

### Requirements

- Python 3.11 or higher
- pip (Python package installer)

### Install Vyte

```bash
pip install vyte
```

### Verify Installation

```bash
vyte --version
```

You should see the version number displayed.

______________________________________________________________________

## Create Your First Project

Let's create a simple FastAPI project with SQLAlchemy and PostgreSQL.

### Interactive Mode (Recommended)

The easiest way to get started is using interactive mode:

```bash
vyte create
```

You'll be prompted for:

1. **Project name** - e.g., "my-api"
1. **Framework** - Choose FastAPI, Flask-Restx, or Django-Rest
1. **ORM** - Choose SQLAlchemy, TortoiseORM, or Peewee
1. **Database** - Choose PostgreSQL, MySQL, or SQLite

### Command-Line Mode

If you prefer, specify all options in one command:

```bash
vyte create my-api --framework FastAPI --orm SQLAlchemy --database PostgreSQL
```

<div class="admonition tip">
<p class="admonition-title">Pro Tip</p>
<p>Use the shorthand flags: <code>-f</code> for framework, <code>-o</code> for ORM, <code>-d</code> for database</p>
</div>

______________________________________________________________________

## Project Structure

After creation, you'll have a fully structured project:

```
my-api/
├── app/
│   ├── __init__.py           # Application factory
│   ├── main.py               # Entry point
│   ├── database.py           # Database configuration
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── users.py      # Example user routes
│   └── models/
│       ├── __init__.py
│       └── user.py           # Example user model
├── alembic/                  # Database migrations
│   ├── versions/
│   └── env.py
├── tests/                    # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   └── test_users.py
├── .env.example              # Environment variables template
├── .gitignore
├── alembic.ini               # Alembic configuration
├── pyproject.toml            # Project dependencies
└── README.md
```

### Key Files

- **app/main.py** - Application entry point
- **app/database.py** - Database connection and session management
- **app/models/** - SQLAlchemy/ORM models
- **app/api/routes/** - API endpoints
- **alembic/** - Database migration scripts
- **.env.example** - Copy this to `.env` and configure

______________________________________________________________________

## Configure Your Database

### 1. Set Up Environment Variables

Copy the example environment file:

```bash
cd my-api
cp .env.example .env
```

### 2. Edit `.env`

Open `.env` and configure your database:

#### For PostgreSQL (Production)

```ini
DATABASE_URL=postgresql://user:password@localhost:5432/my_database
```

#### For SQLite (Development)

```ini
DATABASE_URL=sqlite:///./test.db
```

#### For MySQL

```ini
DATABASE_URL=mysql://user:password@localhost:3306/my_database
```

<div class="admonition warning">
<p class="admonition-title">Important</p>
<p>Never commit your <code>.env</code> file to version control! It's already in <code>.gitignore</code>.</p>
</div>

______________________________________________________________________

## Install Dependencies

### Using pip

```bash
pip install -r requirements.txt
```

### Using Poetry (if configured)

```bash
poetry install
```

______________________________________________________________________

## Run Database Migrations

Before running your application, create the database tables:

```bash
# Generate initial migration
alembic revision --autogenerate -m "Initial migration"

# Apply migrations
alembic upgrade head
```

<div class="admonition info">
<p class="admonition-title">About Alembic</p>
<p>Alembic is a database migration tool that tracks schema changes and applies them safely.</p>
</div>

______________________________________________________________________

## Run Your Application

### FastAPI Projects

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Flask-Restx Projects

```bash
python app/main.py
```

or

```bash
flask run
```

The API will be available at:

- **API**: http://localhost:5000
- **Swagger Docs**: http://localhost:5000/api/doc

______________________________________________________________________

## Test Your API

### Using FastAPI Interactive Docs

1. Open http://localhost:8000/docs in your browser
1. Try the example endpoints (e.g., `/users`)
1. Click "Try it out" to test requests

### Using curl

```bash
# Create a user
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"username": "john", "email": "john@example.com"}'

# Get all users
curl http://localhost:8000/users

# Get a specific user
curl http://localhost:8000/users/1
```

### Using httpie

```bash
# Install httpie
pip install httpie

# Create a user
http POST localhost:8000/users username=john email=john@example.com

# Get all users
http localhost:8000/users
```

______________________________________________________________________

## Run Tests

Your project comes with a basic test suite:

```bash
pytest
```

For coverage report:

```bash
pytest --cov=app tests/
```

______________________________________________________________________

## What's Next?

Now that you have your project running, you can:

### 1. Add More Models

Edit `app/models/` to add your domain models:

```python
# app/models/post.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
```

### 2. Add Routes

Create new route files in `app/api/routes/`:

```python
# app/api/routes/posts.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
def list_posts(db: Session = Depends(get_db)):
    # Your logic here
    pass
```

### 3. Customize Configuration

See the [Configuration Guide](configuration.md) to learn about:

- Environment variables
- Database settings
- Logging configuration
- Security settings

### 4. Deploy Your API

Check out deployment guides for:

- Docker containerization
- Cloud platforms (AWS, GCP, Azure)
- CI/CD pipelines

______________________________________________________________________

## Common Issues

### Database Connection Error

**Problem**: Can't connect to PostgreSQL/MySQL

**Solution**:

1. Make sure the database server is running
1. Check your DATABASE_URL in `.env`
1. Verify username/password are correct
1. Ensure database exists

### Migration Errors

**Problem**: Alembic migration fails

**Solution**:

1. Check database connection first
1. Delete `alembic/versions/*.py` files and regenerate
1. Reset database: `alembic downgrade base` then `alembic upgrade head`

### Import Errors

**Problem**: Module not found errors

**Solution**:

```bash
# Make sure you're in the project directory
cd my-api

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use

**Problem**: Address already in use

**Solution**:

```bash
# Use a different port
uvicorn app.main:app --reload --port 8001
```

______________________________________________________________________

## Need Help?

- 📖 [Configuration Guide](configuration.md)
- 🗄️ [Database Guide](databases.md)
- 🚀 [Framework Comparison](frameworks.md)
- 💬 [GitHub Discussions](https://github.com/yourusername/vyte/discussions)
- 🐛 [Report Issues](https://github.com/yourusername/vyte/issues)

______________________________________________________________________

## Next Steps

- [Configuration](configuration.md) - Learn about customization options
- [Databases](databases.md) - Deep dive into ORMs and databases
- [Frameworks](frameworks.md) - Explore framework-specific features
- [CLI Reference](cli.md) - Complete command documentation
