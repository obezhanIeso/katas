import pytest
from src.main import to_roman


def test_to_roman_returns_I_for_1():
    assert to_roman(1) == 'I'

def test_to_roman_returns_II_for_2():
    assert to_roman(2) == 'II'

def test_to_roman_returns_fundamental_numbers():
    assert to_roman(5) == 'V'
