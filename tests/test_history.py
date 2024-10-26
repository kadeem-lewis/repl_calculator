"""Testing the History class"""

from fractions import Fraction
from app.calculator.history import History
from app.calculator.operations import add, subtract, multiply, divide
from app.calculator.calculation import Calculation


class TestHistory:
    """Test the History class"""

    def setup_method(self):
        """Setup the history for the tests"""
        History.set_history(
            [
                Calculation(Fraction(10), Fraction(5), add),
                Calculation(Fraction(10), Fraction(5), subtract),
                Calculation(Fraction(16), Fraction(2), multiply),
            ]
        )

    def test_get_history(self):
        """Test that get_history returns the history"""
        assert len(History.get_history()) == 3

    def test_set_history(self):
        """Test that set_history sets the history"""
        History.set_history(
            [
                Calculation(Fraction(10), Fraction(5), add),
                Calculation(Fraction(10), Fraction(5), subtract),
            ]
        )
        assert len(History.get_history()) == 2

    def test_add_to_history(self):
        """Test that add_calculation adds a calculation to the history"""
        History.add_calculation(Calculation(Fraction(10), Fraction(5), divide))
        assert len(History.get_history()) == 4

    def test_get_last_calculation(self):
        """Test that get_last_calculation returns the last calculation"""
        last_calculation = History.get_last_calculation()
        assert last_calculation is not None
        assert last_calculation.var_one == Fraction(16)
        assert last_calculation.var_two == Fraction(2)

    def test_clear_history(self):
        """Test that clear_history clears the history"""
        History.clear_history()
        assert len(History.get_history()) == 0
