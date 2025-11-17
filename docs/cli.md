# CLI Commands

Vyte provides a powerful command-line interface with several commands to help you manage your API projects.

## Overview

```bash
vyte [OPTIONS] COMMAND [ARGS]
```

### Global Options

- `--version` - Show version and exit
- `--help` - Show help message and exit

## Commands

### `create`

Create a new API project with interactive prompts or command-line options.

#### Interactive Mode (Recommended)

```bash
vyte create
```

This launches an interactive wizard that guides you through:

1. 📝 **Project Name** - Choose a valid Python package name
1. 🎯 **Framework** - Select Flask-Restx, FastAPI, or Django-Rest
1. 🗄️ **ORM** - Choose SQLAlchemy, TortoiseORM, Peewee, or Django ORM
1. 💾 **Database** - Select PostgreSQL, MySQL, or SQLite
1. 🔐 **Authentication** - Enable JWT authentication (recommended)
1. 🐳 **Docker** - Include Docker configuration (recommended)

#### Non-Interactive Mode

Create a project with all options specified:

```bash
vyte create \
  --no-interactive \
  --name my-api \
  --framework FastAPI \
  --orm SQLAlchemy \
  --database PostgreSQL \
  --auth \
  --docker
```

#### Options

- `--name TEXT` - Project name (required in non-interactive mode)
- `--framework [Flask-Restx|FastAPI|Django-Rest]` - Web framework to use
- `--orm [SQLAlchemy|TortoiseORM|Peewee|Django]` - ORM to use
- `--database [PostgreSQL|MySQL|SQLite]` - Database type
- `--auth / --no-auth` - Include JWT authentication (default: yes)
- `--docker / --no-docker` - Include Docker configuration (default: yes)
- `--no-interactive` - Skip interactive prompts
- `--help` - Show help for this command

#### Examples

**FastAPI with SQLAlchemy and PostgreSQL:**

```bash
vyte create --name blog-api --framework FastAPI --orm SQLAlchemy --database PostgreSQL
```

**Flask-Restx with Peewee and SQLite (no Docker):**

```bash
vyte create --name simple-api --framework Flask-Restx --orm Peewee --database SQLite --no-docker
```

______________________________________________________________________

### `list`

List all available framework, ORM, and database combinations.

```bash
vyte list
```

Shows a table with all compatible combinations and their support status.

#### Output Example

```
╭─────────────────┬──────────────┬────────────┬────────────╮
│ Framework       │ ORM          │ Database   │ Status     │
├─────────────────┼──────────────┼────────────┼────────────┤
│ Flask-Restx     │ SQLAlchemy   │ PostgreSQL │ ✓ Stable   │
│ Flask-Restx     │ SQLAlchemy   │ MySQL      │ ✓ Stable   │
│ Flask-Restx     │ SQLAlchemy   │ SQLite     │ ✓ Stable   │
│ Flask-Restx     │ Peewee       │ SQLite     │ ✓ Stable   │
│ FastAPI         │ SQLAlchemy   │ PostgreSQL │ ✓ Stable   │
│ FastAPI         │ TortoiseORM  │ PostgreSQL │ ✓ Stable   │
╰─────────────────┴──────────────┴────────────┴────────────╯
```

______________________________________________________________________

### `info`

Display detailed information about a specific framework or ORM.

```bash
vyte info [--framework TEXT] [--orm TEXT]
```

#### Options

- `--framework TEXT` - Get info about a framework
- `--orm TEXT` - Get info about an ORM
- `--help` - Show help for this command

#### Examples

**Get FastAPI information:**

```bash
vyte info --framework FastAPI
```

**Get SQLAlchemy information:**

```bash
vyte info --orm SQLAlchemy
```

#### Output Example

```
╭─────────────────── FastAPI Information ───────────────────╮
│                                                           │
│  Type: Modern async web framework                        │
│  Version: 0.104+                                          │
│  Async: Yes                                               │
│  Documentation: https://fastapi.tiangolo.com/            │
│                                                           │
│  Features:                                                │
│  • High performance (based on Starlette and Pydantic)    │
│  • Automatic API documentation                            │
│  • Type hints everywhere                                  │
│  • Async/await support                                    │
│  • Dependency injection                                   │
│                                                           │
│  Compatible ORMs: SQLAlchemy, TortoiseORM                │
│                                                           │
╰───────────────────────────────────────────────────────────╯
```

______________________________________________________________________

### `deps`

Show dependencies for a specific framework, ORM, and database combination.

```bash
vyte deps --framework TEXT --orm TEXT --database TEXT
```

#### Options

- `--framework TEXT` - Framework (required)
- `--orm TEXT` - ORM (required)
- `--database TEXT` - Database (required)
- `--help` - Show help for this command

#### Example

```bash
vyte deps --framework FastAPI --orm SQLAlchemy --database PostgreSQL
```

#### Output Example

```
╭─────────────── Dependencies ───────────────╮
│                                            │
│  Core Dependencies: 8                      │
│  Dev Dependencies: 12                      │
│  Total Size: ~45 MB                        │
│                                            │
│  📦 Core:                                   │
│  • fastapi>=0.104.0                        │
│  • sqlalchemy>=2.0.0                       │
│  • psycopg2-binary>=2.9.9                  │
│  • pydantic>=2.5.0                         │
│  • uvicorn[standard]>=0.24.0               │
│  • python-jose[cryptography]>=3.3.0        │
│  • passlib[bcrypt]>=1.7.4                  │
│  • python-multipart>=0.0.6                 │
│                                            │
│  🔧 Dev:                                    │
│  • pytest>=7.4.3                           │
│  • pytest-asyncio>=0.21.0                  │
│  • httpx>=0.25.0                           │
│  • pytest-cov>=4.1.0                       │
│  ...                                       │
│                                            │
╰────────────────────────────────────────────╯
```

______________________________________________________________________

## Tips & Best Practices

### 🎯 Use Interactive Mode First

If you're new to Vyte, start with the interactive mode:

```bash
vyte create
```

It will guide you through all options and show you compatible combinations.

### 📋 Check Compatibility First

Before creating a project, check available combinations:

```bash
vyte list
```

### 🔍 Learn About Options

Get detailed information about frameworks and ORMs:

```bash
vyte info --framework FastAPI
vyte info --orm SQLAlchemy
```

### 🚀 Save Time with Flags

Once you know your preferred stack, use flags for speed:

```bash
vyte create -n my-api -f FastAPI -o SQLAlchemy -d PostgreSQL
```

### 🐳 Always Include Docker

Docker makes deployment and development easier:

```bash
vyte create --docker  # Default is True
```

### 🔐 Enable Auth for Production

JWT authentication is production-ready:

```bash
vyte create --auth  # Default is True
```

## Next Steps

- [Configuration Guide](configuration.md) - Customize generated projects
- [Integration Guide](integration.md) - Connect with your tools
- [Development Setup](DEVELOPMENT.md) - Set up for contributing
