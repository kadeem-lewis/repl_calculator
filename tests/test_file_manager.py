import pytest
import pandas as pd
import os
from fractions import Fraction
from app.file_manager import FileManager
from app.calculator.calculation import Calculation
from app.calculator.operations import add, subtract
from pytest import MonkeyPatch

@pytest.fixture
def sample_calculations():
    # Create a few sample Calculation instances for testing
    return [
        Calculation(Fraction(2), Fraction(3), add),
        Calculation(Fraction(5), Fraction(2), subtract)
    ]

@pytest.fixture
def temp_csv_file(tmp_path):
    # Create a temporary CSV file for testing purposes
    file_path = tmp_path / "temp.csv"
    return str(file_path)

def test_write_to_csv(temp_csv_file, sample_calculations):
    # Test writing to CSV
    FileManager.write_to_csv(temp_csv_file, sample_calculations)
    
    # Verify that the CSV file is created and contains correct data
    df = pd.read_csv(temp_csv_file)
    assert len(df) == len(sample_calculations)
    assert str(df.iloc[0]['fld_var_one']) == str(sample_calculations[0].var_one)
    assert df.iloc[1]['fld_operation'] == sample_calculations[1].operation.__name__

def test_read_from_csv(monkeypatch: MonkeyPatch, temp_csv_file, sample_calculations):
    # Mock Calculation.from_dict to return items from sample_calculations
    calculations_to_return = iter(sample_calculations)

    def mock_from_dict(data):
        return next(calculations_to_return)

    monkeypatch.setattr(Calculation, 'from_dict', mock_from_dict)

    # Write sample data to CSV
    df = pd.DataFrame([calc.to_dict() for calc in sample_calculations])
    df.to_csv(temp_csv_file, index=False)

    # Test reading from CSV
    calculations = FileManager.read_from_csv(temp_csv_file)
    assert len(calculations) == len(sample_calculations)

def test_read_from_csv_file_not_found():
    # Test read_from_csv with non-existent file
    result = FileManager.read_from_csv("non_existent.csv")
    assert result == []

def test_delete_csv_file(monkeypatch: MonkeyPatch, temp_csv_file):
    # Mock os.remove to verify if it gets called
    def mock_remove(path):
        assert path == temp_csv_file

    monkeypatch.setattr(os, 'remove', mock_remove)

    # Test delete_csv_file
    FileManager.delete_csv_file(temp_csv_file)

def test_delete_csv_file_not_found(monkeypatch: MonkeyPatch):
    # Mock os.remove to raise FileNotFoundError
    def mock_remove(path):
        raise FileNotFoundError

    monkeypatch.setattr(os, 'remove', mock_remove)

    # Test delete_csv_file with non-existent file
    FileManager.delete_csv_file("non_existent.csv")
