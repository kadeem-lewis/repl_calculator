"""Load History command module."""

from app.commands import Command
from app.file_manager import FileManager
from app.calculator.history import History


class LoadHistoryCommand(Command):
    """Command to load the history."""

    def execute(self):
        History.initialize_history()
