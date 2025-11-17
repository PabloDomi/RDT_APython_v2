# ORMs & Databases

Vyte supports multiple ORMs (Object-Relational Mappers) and databases, giving you flexibility in how you interact with your data.

## Supported ORMs

### SQLAlchemy

<div class="admonition tip">
<p class="admonition-title">Most Popular Choice</p>
<p>SQLAlchemy is the most mature and widely-used Python ORM, with excellent documentation and community support.</p>
</div>

**Version**: 2.0+
**Type**: Full-featured ORM
**Async Support**: Yes (2.0+)
**Documentation**: [sqlalchemy.org](https://www.sqlalchemy.org/)

#### Key Features

- 🏗️ **Mature & Stable** - Industry standard for Python ORMs
- ⚡ **Async Support** - Full async/await support in 2.0+
- 🎯 **Type Safety** - Excellent type hints support
- 🔧 **Flexible** - From simple to complex queries
- 📊 **Migrations** - Alembic integration for schema migrations
- 🗄️ **Multi-Database** - PostgreSQL, MySQL, SQLite, and more

#### Best For

- Production applications
- Complex queries and relationships
- When you need migrations (Alembic)
- Both sync and async applications

#### Compatible Frameworks

- ✅ FastAPI (async)
- ✅ Flask-Restx (sync)

#### Example

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
```

______________________________________________________________________

### TortoiseORM

**Version**: 0.20+
**Type**: Async ORM inspired by Django
**Async Support**: Yes (async-first)
**Documentation**: [tortoise.github.io](https://tortoise.github.io/)

#### Key Features

- ⚡ **Async-First** - Designed for async from the ground up
- 🐍 **Pythonic** - Django-like syntax and patterns
- 🎯 **Type Safe** - Full Pydantic integration
- 📦 **Lightweight** - Simpler than SQLAlchemy
- 🔧 **Auto-Migrations** - Built-in Aerich migration tool
- 🗄️ **Multi-Database** - PostgreSQL, MySQL, SQLite

#### Best For

- Async-only applications
- When you like Django ORM syntax
- Microservices and APIs
- Projects with simpler data models

#### Compatible Frameworks

- ✅ FastAPI (async)

#### Example

```python
from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)

    class Meta:
        table = "users"
```

______________________________________________________________________

### Peewee

**Version**: 3.17+
**Type**: Simple, expressive ORM
**Async Support**: No (sync only)
**Documentation**: [peewee.readthedocs.io](http://docs.peewee-orm.com/)

#### Key Features

- 🎯 **Simple** - Easy to learn and use
- 📦 **Lightweight** - Minimal dependencies
- 🔧 **Expressive** - Clean, readable query syntax
- 🗄️ **Multi-Database** - PostgreSQL, MySQL, SQLite
- 📊 **Migrations** - Built-in migration system
- 🎨 **Flask Integration** - Official Flask extension

#### Best For

- Small to medium projects
- When simplicity matters
- SQLite applications
- Learning ORMs
- Quick prototypes

#### Compatible Frameworks

- ✅ Flask-Restx (sync)

#### Example

```python
from peewee import *

database = SqliteDatabase("my_database.db")


class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)

    class Meta:
        database = database
        table_name = "users"
```

______________________________________________________________________

### Django ORM

<div class="admonition warning">
<p class="admonition-title">Coming Soon</p>
<p>Django ORM support will be available when Django Rest Framework is added.</p>
</div>

**Version**: 4.2+
**Type**: Full-featured ORM integrated with Django
**Async Support**: Partial (Django 4.1+)
**Documentation**: [djangoproject.com](https://docs.djangoproject.com/)

______________________________________________________________________

## Supported Databases

### PostgreSQL

<div class="admonition success">
<p class="admonition-title">Production Recommended</p>
<p>PostgreSQL is the recommended choice for production applications.</p>
</div>

**Version**: 12+
**Driver**: psycopg2-binary / asyncpg
**Type**: Advanced relational database

#### Key Features

- 🏢 **Production-Grade** - Battle-tested in enterprise
- ⚡ **Performance** - Excellent performance and scalability
- 🔒 **ACID Compliant** - Full transaction support
- 📊 **Advanced Features** - JSON, arrays, full-text search
- 🔧 **Extensions** - PostGIS, pg_trgm, and more

#### Best For

- Production applications
- Applications needing advanced features
- High-concurrency workloads
- Data integrity is critical

#### Connection String Examples

```python
# Sync (psycopg2)
DATABASE_URL = "postgresql://user:pass@localhost:5432/dbname"

# Async (asyncpg)
DATABASE_URL = "postgresql+asyncpg://user:pass@localhost:5432/dbname"
```

______________________________________________________________________

### MySQL

**Version**: 8.0+
**Driver**: mysqlclient / aiomysql
**Type**: Popular relational database

#### Key Features

- 🌍 **Widely Used** - Popular in web hosting
- 📦 **Easy Setup** - Simple to install and configure
- 🔧 **Good Performance** - Fast for read-heavy workloads
- 💰 **Cost-Effective** - Free and open source

#### Best For

- Shared hosting environments
- Read-heavy applications
- When MySQL is required
- Legacy system integration

#### Connection String Examples

```python
# Sync (mysqlclient)
DATABASE_URL = "mysql://user:pass@localhost:3306/dbname"

# Async (aiomysql)
DATABASE_URL = "mysql+aiomysql://user:pass@localhost:3306/dbname"
```

______________________________________________________________________

### SQLite

**Version**: 3.35+
**Driver**: Built-in Python sqlite3 / aiosqlite
**Type**: Embedded file-based database

#### Key Features

- 📦 **Zero Config** - No server needed
- 🚀 **Fast Development** - Quick to set up and test
- 💾 **Portable** - Single file database
- 🎯 **Simple** - Perfect for learning and prototypes

#### Best For

- Development and testing
- Small applications
- Desktop applications
- Quick prototypes
- Learning and tutorials

#### Connection String Examples

```python
# Sync
DATABASE_URL = "sqlite:///./database.db"

# Async (aiosqlite)
DATABASE_URL = "sqlite+aiosqlite:///./database.db"
```

______________________________________________________________________

## Compatibility Matrix

| Framework       | ORM         | PostgreSQL | MySQL | SQLite |
| --------------- | ----------- | ---------- | ----- | ------ |
| **FastAPI**     | SQLAlchemy  | ✅         | ✅    | ✅     |
| **FastAPI**     | TortoiseORM | ✅         | ✅    | ✅     |
| **Flask-Restx** | SQLAlchemy  | ✅         | ✅    | ✅     |
| **Flask-Restx** | Peewee      | ❌         | ❌    | ✅     |

## Choosing Your Stack

### For Production APIs

**Recommended**: FastAPI + SQLAlchemy + PostgreSQL

```bash
vyte create --framework FastAPI --orm SQLAlchemy --database PostgreSQL
```

### For Quick Prototypes

**Recommended**: Flask-Restx + Peewee + SQLite

```bash
vyte create --framework Flask-Restx --orm Peewee --database SQLite
```

### For Microservices

**Recommended**: FastAPI + TortoiseORM + PostgreSQL

```bash
vyte create --framework FastAPI --orm TortoiseORM --database PostgreSQL
```

### For Learning

**Recommended**: Flask-Restx + SQLAlchemy + SQLite

```bash
vyte create --framework Flask-Restx --orm SQLAlchemy --database SQLite
```

## Next Steps

- [Frameworks](frameworks.md) - Learn about supported frameworks
- [Quick Start](quickstart.md) - Create your first project
- [Configuration](configuration.md) - Customize your setup
