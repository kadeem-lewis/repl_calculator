"""Subtract command plugin"""

import logging
from app.commands import Command
from app.calculator import Calculator


class SubtractCommand(Command):
    """Command to subtract two numbers"""

    def execute(self, num_one, num_two):
        """Subtract two numbers"""
        result = Calculator.subtract(num_one, num_two)
        print(result)
        logging.info(result)