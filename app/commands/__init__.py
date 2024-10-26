"""This module contains the Command and CommandHandler classes"""

import logging
from abc import ABC, abstractmethod
from fractions import Fraction


class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self, *args):
        """Base method for executing a command."""


class CommandHandler:
    """This class is responsible for registering and executing commands."""

    def __init__(self):
        self.commands: dict[str, Command] = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with the handler."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """Execute a command by name."""
        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error("No such command: %s", command_name)

    def get_immediate_commands(self) -> list[str]:
        """Get all immediate command names excluding arithmetic operations."""
        # Define the arithmetic operations to exclude
        operation_commands = ["add", "subtract", "multiply", "divide"]

        # Create a list to keep track of excluded commands
        excluded_commands = []

        # Find and exclude the operation commands and their corresponding index entries
        for command_name in operation_commands:
            if command_name in self.commands:
                excluded_commands.append(command_name)
                # Assuming the next item in the dictionary is the index for the operation
                command_keys = list(self.commands.keys())
                command_index = command_keys.index(command_name)
                if command_index + 1 < len(command_keys):
                    index_key = command_keys[command_index + 1]
                    if index_key.isdigit():
                        excluded_commands.append(index_key)

        # Filter out the excluded commands to get the list of immediate commands
        immediate_commands = [
            command_name for command_name in self.commands.keys()
            if command_name not in excluded_commands
        ]

        return immediate_commands

    