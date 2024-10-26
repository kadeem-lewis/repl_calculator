"""Testing Calculator"""

from fractions import Fraction
from app.calculator import Calculator


def test_addition():
    """Test that addition function works"""
    assert Calculator.add(Fraction(2), Fraction(2)) == Fraction(4)


def test_subtraction():
    """Test that subtraction function works"""
    assert Calculator.subtract(Fraction(2), Fraction(2)) == Fraction(0)


def test_division():
    """Test that division function works"""
    assert Calculator.divide(Fraction(2), Fraction(2)) == Fraction(1)


def test_multiplication():
    """Test that multiplication function works"""
    assert Calculator.multiply(Fraction(2), Fraction(2)) == Fraction(4)
