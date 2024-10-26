"""Clear history command module."""

from app.commands import Command
from app.file_manager import FileManager
from app.calculator.history import History


class ClearHistoryCommand(Command):
    """Command to clear the history."""

    def execute(self):
        History.clear_history()
