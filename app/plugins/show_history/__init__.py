"""Save History command module."""

import logging
from app.commands import Command
from app.calculator.history import History


class SaveHistoryCommand(Command):
    """Command to save the history."""

    def execute(self):
        history = History.get_history()
        if not history:
            logging.info('History is empty.')
        for expression in history:
            print(expression)
