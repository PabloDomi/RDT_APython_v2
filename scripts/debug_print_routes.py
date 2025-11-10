import tempfile, os, sys
from pathlib import Path
from rdt.core.config import ProjectConfig
from rdt.core.generator import ProjectGenerator
import importlib

temp_dir = Path(tempfile.mkdtemp())
orig = os.getcwd()
os.chdir(temp_dir)
config = ProjectConfig(
    name='inproc-debug', framework='FastAPI', orm='SQLAlchemy', database='SQLite', auth_enabled=False, docker_support=False, testing_suite=True, git_init=False
)
print('Generating in', temp_dir)
pg = ProjectGenerator()
proj = pg.generate(config)
print('project', proj)
# write stubs
src = proj / 'src'
(src / 'database.py').write_text('''async def init_db():\n    return None\n\nasync def close_db():\n    return None\n\nasync def get_db():\n    try:\n        yield None\n    finally:\n        return\n''')
(src / 'api' / 'routes.py').write_text('''from fastapi import APIRouter\nrouter = APIRouter()\n@router.get('/items')\nasync def list_items():\n    return []\n''')
sys.path.insert(0, str(proj))
mod = importlib.import_module('src.main')
app = getattr(mod, 'app')
print('routes:')
for r in app.routes:
    print(r.path, getattr(r, 'methods', None))
os.chdir(orig)
