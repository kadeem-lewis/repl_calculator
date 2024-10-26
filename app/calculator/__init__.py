"Main calculator code"
from fractions import Fraction
from app.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculation import Calculation, OperationFunction
from app.calculator.history import History


class Calculator:
    """Class responsible for the calculator operations"""

    @staticmethod
    def perform_calculation(
        var_one: Fraction, var_two: Fraction, operation: OperationFunction
    ) -> Fraction:
        """Perform a calculation and store it in history"""
        calculation = Calculation(var_one, var_two, operation)
        History.add_calculation(calculation)
        return calculation.calculate()

    @staticmethod
    def add(addend_one: Fraction, addend_two: Fraction) -> Fraction:
        """Add two numbers"""
        return Calculator.perform_calculation(addend_one, addend_two, add)

    @staticmethod
    def subtract(minuend: Fraction, subtrahend: Fraction) -> Fraction:
        """Subtract two numbers"""
        return Calculator.perform_calculation(minuend, subtrahend, subtract)

    @staticmethod
    def multiply(multiplier: Fraction, multiplicand: Fraction) -> Fraction:
        """Multiply two numbers"""
        return Calculator.perform_calculation(multiplier, multiplicand, multiply)

    @staticmethod
    def divide(dividend: Fraction, divisor: Fraction) -> Fraction:
        """Divide two numbers"""
        return Calculator.perform_calculation(dividend, divisor, divide)
