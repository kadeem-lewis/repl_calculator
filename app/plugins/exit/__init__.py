"""Exit command module."""

import sys
from app.commands import Command


class ExitCommand(Command):
    """Command to exit the application."""

    def execute(self):
        sys.exit("Exiting...")