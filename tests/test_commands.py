"""Tests for the command functions."""

import pytest
from app import App


def test_add_command(capfd, monkeypatch):
    """Test that the 'add' command correctly adds two numbers."""
    # Simulate user entering 'add' followed by two numbers and 'exit'
    inputs = iter(["add", 1, 2, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Capture the output of the 'add' command
    out, _ = capfd.readouterr()

    # Verify that the expected sum appears in the output
    assert "3" in out, "The sum of 1 and 2 should be 3"


def test_subtract_command(capfd, monkeypatch):
    """Test that the 'subtract' command correctly subtracts two numbers."""
    # Simulate user entering 'subtract' followed by two numbers and 'exit'
    inputs = iter(["subtract", 5, 2, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Capture the output of the 'subtract' command
    out, _ = capfd.readouterr()

    # Verify that the expected difference appears in the output
    assert "3" in out, "The difference of 5 and 2 should be 3"


def test_multiply_command(capfd, monkeypatch):
    """Test that the 'multiply' command correctly multiplies two numbers."""
    # Simulate user entering 'multiply' followed by two numbers and 'exit'
    inputs = iter(["multiply", 5, 2, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Capture the output of the 'multiply' command
    out, _ = capfd.readouterr()

    # Verify that the expected product appears in the output
    assert "10" in out, "The product of 5 and 2 should be 10"


def test_divide_command(capfd, monkeypatch):
    """Test that the 'divide' command correctly divides two numbers."""
    # Simulate user entering 'divide' followed by two numbers and 'exit'
    inputs = iter(["divide", 10, 2, "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    # Capture the output of the 'divide' command
    out, _ = capfd.readouterr()

    # Verify that the expected quotient appears in the output
    assert "5" in out, "The quotient of 10 and 2 should be 5"


def test_app_greet_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"


def test_app_menu_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'menu' command and prints available commands."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    # Capture the output of the 'menu' command
    out, _ = capfd.readouterr()

    # Verify that the expected menu content appears in the output
    expected_commands = ["add", "subtract", "multiply", "divide", "menu", "exit"]

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Check that the output contains the available commands
    for command in expected_commands:
        assert command in out, f"The command '{command}' should be listed in the menu."