"""Module to hold the history of all calculations performed by the calculator."""

from typing import List, Optional
from app.calculator.calculation import Calculation


class History:
    """Class to hold the history of all calculations performed by the calculator."""

    _history: List[Calculation] = []

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
    def add_calculation(cls, calculation: Calculation):
        """Add a calculation to the history."""
        cls._history.append(calculation)

    @classmethod
    def clear_history(cls):
        """Clear the history of all calculations."""
        cls._history.clear()

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Return the last calculation performed."""
        return cls._history[-1] if cls._history else None
