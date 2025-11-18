# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.5] - 2025-11-17

### Added

- **Comprehensive MkDocs documentation website** with Material theme
  - 7 complete documentation pages: index, quickstart, cli, frameworks, databases, configuration, api-reference
  - Professional Material theme with custom colors (cyan/deep purple)
  - Integrated Vyte logos in header and favicon
  - Search functionality
  - Git revision date plugin for last modified timestamps
  - mkdocstrings for automatic API documentation
  - Full navigation structure with 6 main sections
- **GitHub Actions workflow for automatic documentation deployment**
  - Automatic deployment to GitHub Pages on push to main
  - Triggered by changes in docs/, mkdocs.yml, or source code
  - Python dependency caching for faster builds
- **Documentation dependencies** in pyproject.toml
  - mkdocs >= 1.5.0
  - mkdocs-material >= 9.5.0
  - mkdocstrings\[python\] >= 0.24.0
  - mkdocs-git-revision-date-localized-plugin >= 1.2.0
- **Branding assets**
  - 5 logo variants in docs/images/ folder
  - BRANDING.md guide for logo usage
  - Documentation badge in README.md

### Fixed

- Logo visibility in documentation header (changed to B&W version for better contrast)
- Broken links in documentation files (README.md, docs/ paths)
- Logo path in index.md (corrected to relative images/ path)
- MkDocs build warnings and strict mode errors

### Changed

- Added documentation link badge to README.md
- Copied SECURITY.md to docs/ folder for MkDocs access
- Added site/ folder to .gitignore
- Updated mkdocs.yml to use B&W logo for better header contrast

### Documentation

- **Quick Start Guide**: Complete installation and first project tutorial
- **CLI Reference**: Full command documentation with examples and tips
- **Frameworks Guide**: Detailed comparison of FastAPI, Flask-Restx, Django-Rest
- **Databases Guide**: Comprehensive ORM and database documentation
- **Configuration Guide**: Environment variables and settings reference
- **API Reference**: Complete Python API documentation
- **Home Page**: Feature overview, philosophy, and use cases

## [2.0.4] - 2025-11-13

### Added

- Custom exception hierarchy with 8 specific exception types (VyteError, ConfigurationError, GenerationError, TemplateError, DependencyError, ValidationError, FileSystemError, GitError)
- Comprehensive test suite for exceptions with 100% coverage
- 26 new unit tests for display functions and interactive mode
- Pre-commit hooks configuration with black, ruff, isort, bandit, and mypy
- EditorConfig file for consistent coding styles
- Pylint configuration file
- GitHub Actions workflow for automated testing and linting
- CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, CONTRIBUTORS.md, DEVELOPMENT.md, and ROADMAP.md documentation
- Codecov configuration for code coverage tracking
- .gitattributes for consistent line endings
- Improved Makefile with 20+ development commands

### Fixed

- Synchronized version numbers across all files (2.0.4)
- Fixed CLI help command displaying correct name 'vyte' instead of 'cli'
- Improved version management using single source of truth in `__version__.py`
- Better error handling with specific exception types instead of generic Exception
- PackageLoader exception handling in renderer module

### Changed

- Version now imported dynamically from `__version__.py` across all modules
- Converted pyproject.toml to use setuptools with dynamic version attribute
- Improved code consistency and formatting (31 files reformatted with black)
- Enhanced error messages with custom exception types
- Updated README.md with badges and comprehensive project information
- Reorganized documentation files into dedicated docs/ folder
- Moved SECURITY.md to root for GitHub security tab integration

### Improved

- Test coverage increased from 72% to 73% (65 tests total: 63 passed, 2 skipped)
- Code quality with automated linting and formatting tools
- Developer experience with pre-commit hooks and improved documentation
- Project structure and organization for better maintainability

## [2.0.3] - 2025-11-XX

### Added

- Multiple framework support (Flask-Restx, FastAPI, Django-Rest)
- Multiple ORM support (SQLAlchemy, TortoiseORM, Peewee, Django ORM)
- Interactive CLI with beautiful Rich UI
- JWT authentication support
- Docker and docker-compose generation
- Complete testing suite with pytest
- Auto-generated API documentation
- Git repository initialization

### Changed

- Migrated to Pydantic v2
- Updated to Python 3.11+ requirement
- Improved project structure and organization

## [2.0.0] - 2025-10-XX

### Added

- Initial release of Vyte 2.0
- Complete rewrite with modern Python practices
- Support for async frameworks
- Comprehensive compatibility matrix
- Template-based generation system

## \[1.x.x\] - Legacy

Previous versions (deprecated)

______________________________________________________________________

## Version Comparison

### \[Unreleased\]

- Features and fixes in development

### Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes

[2.0.0]: https://github.com/PabloDomi/Vyte/releases/tag/v2.0.0
[2.0.3]: https://github.com/PabloDomi/Vyte/compare/v2.0.0...v2.0.3
[2.0.4]: https://github.com/PabloDomi/Vyte/compare/v2.0.3...v2.0.4
[2.0.5]: https://github.com/PabloDomi/Vyte/compare/v2.0.4...v2.0.5
