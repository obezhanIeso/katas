import pytest
from src.main import to_roman, divide


def test_to_roman_returns_I_for_1():
    assert to_roman(1) == 'I'

def test_to_roman_returns_II_for_2():
    assert to_roman(2) == 'II'

def test_to_roman_returns_V_for_5():
    assert to_roman(5) == 'V'

def test_to_roman_returns_X_for_10():
    assert to_roman(10) == 'X'
    
def test_to_roman_returns_L_for_50():
    assert to_roman(50) == 'L'
    
def test_to_roman_returns_C_for_100():
    assert to_roman(100) == 'C'
    
def test_to_roman_returns_D_for_500():
    assert to_roman(500) == 'D'
    
def test_to_roman_returns_M_for_1000():
    assert to_roman(1000) == 'M'
    
def test_to_roman_returns_MM_for_2000():
    assert to_roman(2000) == 'MM'

def test_divide_returns_1_for_1():
    assert divide(1) == 1

def test_divide_returns_1_for_10():
    assert divide(10) == 1

def test_divide_returns_1_for_100():
    assert divide(100) == 1

def test_divide_returns_1_for_1000():
    assert divide(1000) == 1

def test_to_roman_returns_IV_for_4():
    assert to_roman(4) == 'IV'

def test_to_roman_returns_MM_for_3000():
    assert to_roman(3000) == 'MMM'

def test_to_roman_returns_CC_for_200():
    assert to_roman(200) == 'CC'

def test_to_roman_returns_CCC_for_300():
    assert to_roman(300) == 'CCC'