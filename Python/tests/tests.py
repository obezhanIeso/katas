import pytest
from src.main import to_roman


def test_check_to_roman():
    assert to_roman(1) == 'I'
