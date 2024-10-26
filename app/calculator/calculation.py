"""Module providing class for calculation of variables"""

from typing import Callable
from fractions import Fraction
from app.calculator.operations import add, subtract, multiply, divide

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

    def to_dict(self):
        """Serialize the Calculation to a dictionary"""
        return {
            'fld_var_one': str(self.var_one),
            'fld_var_two': str(self.var_two),
            'fld_operation': self.operation.__name__,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Deserialize a Calculation from a dictionary"""
        var_one = Fraction(data['fld_var_one'])
        var_two = Fraction(data['fld_var_two'])
        operation_name = data['fld_operation']
        operation = cls.get_operation_by_name(operation_name)
        return cls(var_one, var_two, operation)

    @staticmethod
    def get_operation_by_name(name: str) -> OperationFunction:
        """Get the operation function by its name"""
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
        }
        return operations.get(name)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.var_one}, {self.var_two}, {self.operation.__name__})"
