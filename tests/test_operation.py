"""Operations Test"""

from fractions import Fraction
import pytest
from app.calculator import add, subtract, divide, multiply


def test_addition():
    """Test that addition function works"""
    assert add(Fraction(2), Fraction(2)) == 4


def test_subtraction():
    """Test that subtraction function works"""
    assert subtract(Fraction(2), Fraction(2)) == 0


def test_division():
    """Test that division function works"""
    assert divide(Fraction(2), Fraction(2)) == 1


def test_multiplication():
    """Test that multiplication function works"""
    assert multiply(Fraction(2), Fraction(2)) == 4


def test_divide_by_zero():
    """Test that division by zero raises an error"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(Fraction(2), Fraction(0))
