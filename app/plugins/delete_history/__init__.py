"""Delete history command module."""

from app.commands import Command
from app.file_manager import FileManager
from app.calculator.history import History


class DeleteHistoryCommand(Command):
    """Command to delete the history."""

    def execute(self):
        History.clear_history()
        FileManager.delete_csv_file(History.get_history_path())
