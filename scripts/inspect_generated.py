import tempfile
import os
from pathlib import Path

from rdt.core.generator import ProjectGenerator
from rdt.core.config import ProjectConfig

config = ProjectConfig(
    name="integration-test",
    framework="FastAPI",
    orm="TortoiseORM",
    database="PostgreSQL",
    auth_enabled=True,
    docker_support=True,
    testing_suite=True,
    git_init=False,
)

generator = ProjectGenerator()

temp_dir = Path(tempfile.mkdtemp())
print(f"Generating to {temp_dir}")
original = os.getcwd()
try:
    os.chdir(temp_dir)
    project_path = generator.generate(config)
    models_file = project_path / 'src' / 'models' / 'models.py'
    schemas_file = project_path / 'src' / 'schemas' / 'schemas.py'
    print(f"Models file: {models_file}\n")
    print(models_file.read_text(encoding='utf-8'))
    print('\n' + '='*60 + '\n')
    print(f"Schemas file: {schemas_file}\n")
    print(schemas_file.read_text(encoding='utf-8'))
finally:
    os.chdir(original)
