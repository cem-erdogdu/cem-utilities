import subprocess
import sys


def test_cli_hello_runs():
    result = subprocess.run(
        [sys.executable, "-m", "cem_utils.cli", "hello", "--name", "Test"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Hello, Test!" in result.stdout
