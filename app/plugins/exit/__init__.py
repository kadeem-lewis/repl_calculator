"""Exit command module."""

import sys
import os
from app.commands import Command
from app.file_manager import FileManager
from app.calculator.history import History


class ExitCommand(Command):
    """Command to exit the application."""

    def execute(self):
        History.save_history()
        sys.exit("Exiting...")
        