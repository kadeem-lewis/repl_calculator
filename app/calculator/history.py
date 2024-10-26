"""Module to hold the history of all calculations performed by the calculator."""
import os
import logging
from typing import List, Optional
from app.calculator.calculation import Calculation
from app.file_manager import FileManager


class History:
    """Class to hold the history of all calculations performed by the calculator."""

    _history: List[Calculation] = []
    file_path = os.environ.get("HISTORY_PATH")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Return the history of all calculations."""
        return cls._history

    @classmethod
    def set_history(cls, history: List[Calculation]):
        """Set the history of all calculations."""
        cls._history.clear()
        cls._history.extend(history)

    @classmethod
    def get_history_path(cls):
        """Return the path to the history file."""
        if cls.file_path is None:
            logging.error("Error: HISTORY_PATH environment variable is not set.")
            return

        return os.path.abspath(cls.file_path)

    @classmethod
    def initialize_history(cls):
        """Initialize the history from a CSV file."""
        cls._history = FileManager.read_from_csv(cls.get_history_path())
        logging.info("History initialized with %d calculations.", len(cls._history))


    @classmethod
    def save_history(cls):
        """Save the history to a CSV file."""
        FileManager.write_to_csv(cls.get_history_path(), cls._history)
        logging.info("History saved to %s.", cls.get_history_path())


    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a calculation to the history."""
        cls._history.append(calculation)
        logging.info("Calculation added to history: %s", calculation)

    @classmethod
    def clear_history(cls):
        """Clear the history of all calculations."""
        cls._history.clear()

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Return the last calculation performed."""
        return cls._history[-1] if cls._history else None
