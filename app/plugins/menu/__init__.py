"""Module to display the list of available commands."""

import logging
from app.commands import Command, CommandHandler


class MenuCommand(Command):
    """Command to display the list of available commands."""

    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        commands_list = [
            command_name
            for command_name in self.command_handler.commands.keys()
            if not command_name.isdigit()
        ]
        if commands_list:
            logging.info("Available commands:")
            for index, command_name in enumerate(commands_list, start=1):
                print(f"{index}. {command_name}")