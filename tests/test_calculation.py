from fractions import Fraction
from app.calculator import Calculation
from app.calculator.operations import add


def test_calculation(var_one, var_two, operation, expected):
    """Test that calculation calculate function works"""
    assert Calculation(var_one, var_two, operation).calculate() == expected


def test_calculation_repr():
    """Test that calculation repr function works"""
    assert repr(Calculation(Fraction(2), Fraction(2), add)) == "Calculation(2, 2, add)"
