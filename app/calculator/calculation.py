"""Module providing class for calculation of variables"""

from typing import Callable
from fractions import Fraction

OperationFunction = Callable[[Fraction, Fraction], Fraction]


class Calculation:
    """This class handles the calculation of variables"""

    def __init__(
        self,
        var_one: Fraction,
        var_two: Fraction,
        operation: OperationFunction,
    ):
        self.var_one = var_one
        self.var_two = var_two
        self.operation = operation

    def calculate(self) -> Fraction:
        """Calculate the result of the operation"""
        return self.operation(self.var_one, self.var_two)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.var_one}, {self.var_two}, {self.operation.__name__})"
