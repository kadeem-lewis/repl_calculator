"""Exit command module."""

import sys
from app.commands import Command
from app.file_manager import FileManager
from app.calculator.history import History


class ExitCommand(Command):
    """Command to exit the application."""

    def execute(self):
        sys.exit("Exiting...")
        