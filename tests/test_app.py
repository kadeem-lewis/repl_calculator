import pytest
from app import App


def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit


def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(["unknown_command", 1, 2, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Verify that the unknown command was handled as expected
    out, _ = capfd.readouterr()
    assert "No such command: unknown_command" in out


def test_not_number_value(capfd, monkeypatch):
    """Test that the REPL handles non-number input."""
    # Simulate user entering 'add', followed by a non-number value, then 'exit'
    inputs = iter(["add", "not_a_number", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Verify that the error message appears in the output
    out, _ = capfd.readouterr()
    assert "Invalid input. Please enter a number." in out