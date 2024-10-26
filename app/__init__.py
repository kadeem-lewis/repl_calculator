""" Main application module. """

import os
import sys
from fractions import Fraction
import logging
import logging.config
import pkgutil
import importlib
from dotenv import load_dotenv
from app.commands import CommandHandler, Command
from app.calculator.history import History
class App:
    """ Main application class. """
    def __init__(self):
        """ Initialize the application. """
        os.makedirs("logs", exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault("ENVIRONMENT", "PRODUCTION")
        self.command_handler = CommandHandler()
        History.initialize_history()

    def configure_logging(self):
        """Configure logging."""
        logging_conf_path = "logging.conf"
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
            )
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = "ENVIRONMENT"):
        """Get an environment variable."""
        return self.settings.get(env_var, None)

    def load_plugins(self):
        """Dynamically load all plugins in the plugins directory"""
        plugins_package = "app.plugins"
        for index, (_, plugin_name, is_pkg) in enumerate(
            pkgutil.iter_modules([plugins_package.replace(".", "/")]), start=1
        ):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(
                    f"{plugins_package}.{plugin_name}"
                )
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(
                            item, (Command)
                        ):  # Assuming a BaseCommand class exists
                            if plugin_name == "menu":
                                self.command_handler.register_command(
                                    plugin_name, item(self.command_handler)
                                )
                                self.command_handler.register_command(
                                    str(index), item(self.command_handler)
                                )
                            else:
                                self.command_handler.register_command(
                                    plugin_name, item()
                                )
                                self.command_handler.register_command(
                                    str(index), item()
                                )
                    except TypeError:
                        continue  # If item is not a

    def start(self):
        """ Start the application. """
        self.load_plugins()

        logging.info("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            command = (
                input(
                    "Enter a command (add, subtract, multiply, divide),  'exit' to quit or 'menu' to see available commands: "
                )
                .strip()
                .lower()
            )
            if command in ["exit", "menu"]:
                self.command_handler.execute_command(command)
                continue
            try:
                number_one = Fraction(input("Enter first number: "))
                number_two = Fraction(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                logging.error("Invalid input. Please enter a number.")
                continue
            self.command_handler.execute_command(command, number_one, number_two)