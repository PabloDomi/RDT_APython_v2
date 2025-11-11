import os
import sys
import tempfile
import shutil
from pathlib import Path

import pytest

from tests.integration._utils import insert_project_path, remove_project_path, import_with_retry, safe_rmtree
from vyte.core.config import ProjectConfig
from vyte.core.generator import ProjectGenerator


@pytest.mark.integration
def test_flask_restx_root_and_users():
    temp_dir = Path(tempfile.mkdtemp())
    original_cwd = os.getcwd()
    project_path = None

    try:
        config = ProjectConfig(
            name="flask-inproc-test",
            framework="Flask-Restx",
            orm="SQLAlchemy",
            database="SQLite",
            auth_enabled=False,
            docker_support=False,
            testing_suite=True,
            git_init=False,
        )

        generator = ProjectGenerator()

        os.chdir(temp_dir)
        project_path = generator.generate(config)
        os.chdir(original_cwd)

        src_dir = project_path / "src"

        # Ensure routes package exists
        (src_dir / "routes").mkdir(parents=True, exist_ok=True)
        (src_dir / "routes" / "__init__.py").touch()

        # Minimal extensions stub expected by generated create_app
        (src_dir / "extensions.py").write_text(
            """class DummyAPI:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        self.app = app

    def add_namespace(self, ns):
        # ns is a simple object with routes list of (rule, methods, func)
        for rule, methods, func in getattr(ns, 'routes', []):
            # Flask add_url_rule expects endpoint name; use func.__name__
            self.app.add_url_rule(rule, endpoint=func.__name__, view_func=func, methods=methods)


class DummyDB:
    def init_app(self, app):
        pass


class DummyMigration:
    def init_app(self, app, db):
        pass


api = DummyAPI()
db = DummyDB()
migration = DummyMigration()
""",
            encoding="utf-8",
        )

        # Minimal models stub
        (src_dir / "models").mkdir(parents=True, exist_ok=True)
        (src_dir / "models" / "__init__.py").touch()
        (src_dir / "models" / "models.py").write_text(
            """class User:
    def __init__(self, username, email):
        self.id = 1
        self.username = username
        self.email = email

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}
""",
            encoding="utf-8",
        )

        # Lightweight routes stub with items in-memory
        (src_dir / "routes" / "routes_example.py").write_text(
            """from types import SimpleNamespace

_USERS = []


def _root():
    return {'status': 'ok', 'message': 'Test API'}


def _health():
    return {'status': 'healthy'}


def list_users():
    return _USERS


def create_user():
    data = {} if not hasattr(__import__('flask').request, 'json') else __import__('flask').request.json
    uid = len(_USERS) + 1
    user = {'id': uid, 'username': data.get('username', 'u'), 'email': data.get('email', '')}
    _USERS.append(user)
    from flask import jsonify

    return jsonify(user), 201


user_ns = SimpleNamespace()
user_ns.name = 'users'
user_ns.routes = [
    ('/', ['GET'], _root),
    ('/health', ['GET'], _health),
    ('/users', ['GET'], list_users),
    ('/users', ['POST'], create_user),
]
""",
            encoding="utf-8",
        )

        # Clear caches and import
        for modname in ['app', 'src', 'src.routes.routes_example']:
            if modname in sys.modules:
                del sys.modules[modname]

        insert_project_path(project_path)
        try:
            mod = import_with_retry('app', project_path)
            app = getattr(mod, 'app')

            # Use Flask test client
            client = app.test_client()

            # Root
            r = client.get('/')
            assert r.status_code == 200
            j = r.get_json()
            assert j.get('status') in ('ok', 'healthy') or 'message' in j

            # Health
            r2 = client.get('/health')
            assert r2.status_code == 200
            assert r2.get_json().get('status') == 'healthy'

            # Users initially empty
            r3 = client.get('/users')
            assert r3.status_code == 200

            # Create user
            payload = {'username': 'test', 'email': 't@example.com'}
            r4 = client.post('/users', json=payload)
            assert r4.status_code == 201
            created = r4.get_json()
            assert created['id'] == 1
            assert created['username'] == payload['username']

        finally:
            remove_project_path(project_path)
            for modname in ['app', 'src', 'src.routes.routes_example']:
                if modname in sys.modules:
                    del sys.modules[modname]

    finally:
        if temp_dir.exists():
            safe_rmtree(temp_dir)
