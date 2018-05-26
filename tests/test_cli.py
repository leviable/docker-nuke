import mock

from click.testing import CliRunner
import pytest

from dockernuke.cli import cli


@pytest.fixture()
def cli_tester():
    """ CLI fixture """
    runner = CliRunner()

    def test_cli(*cli_args):
        return runner.invoke(cli, cli_args)

    return test_cli


@mock.patch('dockernuke.cli.nuke')
def test_cli_no_flags(nuke_mock, cli_tester):
    """ Verify CLI call with no options """
    result = cli_tester()

    assert result.exit_code == 0
    assert nuke_mock.call_args == mock.call(force=False)


@mock.patch('dockernuke.cli.nuke')
def test_cli_w_no_force(nuke_mock, cli_tester):
    """ Verify CLI call with --no-force option """
    result = cli_tester(*["--no-force"])

    assert result.exit_code == 0
    assert nuke_mock.call_args == mock.call(force=False)


@mock.patch('dockernuke.cli.nuke')
def test_cli_w_force(nuke_mock, cli_tester):
    """ Verify cli call with --force option """
    result = cli_tester(*["--force"])

    assert result.exit_code == 0
    assert nuke_mock.call_args == mock.call(force=True)
