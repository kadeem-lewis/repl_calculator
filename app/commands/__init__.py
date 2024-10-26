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

        # Collect command instances for arithmetic operations
        operation_instances = {
            command_name: self.commands[command_name]
            for command_name in operation_commands
            if command_name in self.commands
        }

        # Filter out commands that match the instances of arithmetic operations
        immediate_commands = [
            command_name for command_name, command_instance in self.commands.items()
            if command_instance not in operation_instances.values()
        ]

        return immediate_commands