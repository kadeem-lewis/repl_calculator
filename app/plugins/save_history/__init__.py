"""Save History command module."""

from app.commands import Command
from app.calculator.history import History


class SaveHistoryCommand(Command):
    """Command to save the history."""

    def execute(self):
        History.save_history()
