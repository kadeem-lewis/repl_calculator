"""Multiply command plugin"""

import logging
from app.commands import Command
from app.calculator import Calculator


class MultiplyCommand(Command):
    """Command to multiply two numbers"""

    def execute(self, num_one, num_two):
        """Multiply two numbers"""
        result = Calculator.multiply(num_one, num_two)
        print(result)
        logging.info(result)