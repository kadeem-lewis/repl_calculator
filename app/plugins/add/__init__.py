"""Add command plugin"""

import logging
from app.commands import Command
from app.calculator import Calculator


class AddCommand(Command):
    """Command to add two numbers"""

    def execute(self, num_one, num_two):
        """Add two numbers"""
        result = Calculator.add(num_one, num_two)
        print(result)
        logging.info(result)