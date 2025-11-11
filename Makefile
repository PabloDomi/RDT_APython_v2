"""
# Makefile

.PHONY: test test-cov test-integration install clean

test:
	pytest -v

test-cov:
	pytest --cov=presto --cov-report=html --cov-report=term-missing

test-integration:
	pytest -v -m integration

test-all:
	pytest -v --cov=presto --cov-report=html

install:
	pip install -e .
	pip install -r requirements-dev.txt

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

format:
	black presto/ tests/
	ruff check --fix presto/ tests/

lint:
	black --check presto/ tests/
	ruff check presto/ tests/
	mypy presto/

pre-commit:
	pre-commit run --all-files
"""