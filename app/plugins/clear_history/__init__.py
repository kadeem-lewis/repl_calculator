"""Clear history command module."""

import logging
from app.commands import Command
from app.calculator.history import History


class ClearHistoryCommand(Command):
    """Command to clear the history."""

    def execute(self):
        History.clear_history()
        logging.info("History cleared.")
