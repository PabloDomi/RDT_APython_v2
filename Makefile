"""
# Makefile

.PHONY: test test-cov test-integration test-all install clean format lint pre-commit help

test:
	pytest -q

test-cov:
	pytest --cov=vyte --cov-report=html --cov-report=term-missing

test-integration:
	pytest -v -m integration

test-all:
	pytest -v --cov=vyte --cov-report=html

install:
	# Use the active Python interpreter's pip to ensure correct environment
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e .
	python -m pip install -r requirements-dev.txt

clean:
	# Remove build artifacts and temporary test files
	rm -rf build/ dist/ *.egg-info htmlcov/ .pytest_cache/ .coverage
	# Remove Python cache files
	find . -type d -name __pycache__ -exec rm -rf {} + || true
	find . -type f -name "*.pyc" -delete || true

format:
	# Format Python code (Black) then let Ruff auto-fix lint issues
	black vyte/ tests/
	ruff check --fix vyte/ tests/ || true

lint:
	black --check vyte/ tests/
	ruff check vyte/ tests/
	mypy vyte/

pre-commit:
	pre-commit run --all-files || true

help:
	@echo "Makefile targets:"
	@echo "  test            - Run unit tests (pytest)"
	@echo "  test-cov        - Run tests with coverage report"
	@echo "  test-integration- Run only integration tests (pytest -m integration)"
	@echo "  test-all        - Run all tests with coverage"
	@echo "  install         - Install package in editable mode and dev deps"
	@echo "  clean           - Remove build and temporary files"
	@echo "  format          - Run code formatters (black + ruff)"
	@echo "  lint            - Run linters and mypy"
	@echo "  pre-commit      - Run pre-commit hooks"
	@echo "  help            - Show this help message"
"""