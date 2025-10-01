# Test

> API project generated with RDT v2.0

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL server
### Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
nano .env
```

### Database Setup

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Run Server

```bash
python app.py
```

Visit: http://localhost:5300
## 🧪 Testing

```bash
pytest
pytest --cov=src
```

## 🐳 Docker

```bash
docker-compose up -d
```

## 📚 Documentation

- Framework: [Flask-Restx](https://flaskrestx.com)
- ORM: [SQLAlchemy](https://sqlalchemy.org)

## 📝 License

MIT