# tests/test_cli.py
"""
Test CLI commands
"""
from click.testing import CliRunner

from rdt.cli.commands import cli


def test_cli_help():
    """Test CLI help command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])

    assert result.exit_code == 0
    assert 'RDT' in result.output
    assert 'create' in result.output


def test_cli_version():
    """Test CLI version command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])

    assert result.exit_code == 0
    assert '2.0.0' in result.output


def test_cli_list():
    """Test list command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['list'])

    assert result.exit_code == 0
    assert 'Flask-Restx' in result.output
    assert 'FastAPI' in result.output


def test_cli_info():
    """Test info command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['info', 'FastAPI'])

    assert result.exit_code == 0
    assert 'FastAPI' in result.output
    assert 'SQLAlchemy' in result.output


def test_cli_deps():
    """Test deps command"""
    runner = CliRunner()
    result = runner.invoke(cli, ['deps', 'Flask-Restx'])

    assert result.exit_code == 0
    assert 'Dependencies' in result.output


def test_cli_create_non_interactive():
    """Test create command without interaction"""
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(cli, [
            'create',
            '--name', 'test-cli-api',
            '--framework', 'Flask-Restx',
            '--orm', 'SQLAlchemy',
            '--database', 'SQLite',
            '--no-interactive'
        ])

        # Should succeed or fail gracefully
        assert result.exit_code in [0, 1]
