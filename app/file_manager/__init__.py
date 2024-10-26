"""Module for reading and writing csvs."""

from typing import List
import pandas as pd
from app.calculator.calculation import Calculation

class FileManager:
    """Class for reading and writing csvs."""
    @staticmethod
    def read_from_csv(file_name: str) -> List[Calculation]:
        """Read data from a CSV file and return it as a list of Calculations."""
        try:
            df = pd.read_csv(file_name)
        except FileNotFoundError:
            return []

        calculations = []
        for _, row in df.iterrows():
            try:
                calc = Calculation.from_dict(row.to_dict())
                calculations.append(calc)
            except Exception as e:
                # Handle any parsing errors
                print(f"Error parsing row {row}: {e}")
        return calculations

    @staticmethod
    def write_to_csv(file_name: str, calculations: List[Calculation]):
        """Write a list of Calculations to a CSV file using Pandas."""
        data = [calc.to_dict() for calc in calculations]
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        