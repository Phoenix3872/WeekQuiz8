import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import Calculator
import math
import pytest


calc = Calculator()

def test_add():
    assert calc.add(5, 6) == 11

def test_add2():
    assert calc.add(5, 6) != 10

def test_subtract():
    assert calc.subtract(10, 3) == 7
    assert calc.subtract(0, 5) == -5

def test_multiply():
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(0, 99) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-9, 3) == -3
    with pytest.raises(ValueError):
        calc.divide(1, 0)

def test_log():
    assert calc.log(1) == 0
    assert round(calc.log(math.e), 6) == 1
    with pytest.raises(ValueError):
        calc.log(0)
    with pytest.raises(ValueError):
        calc.log(-5)

def test_square():
    assert calc.square(5) == 25
    assert calc.square(-4) == 16
    assert calc.square(0) == 0

def test_sin():
    assert calc.sin(0) == 0

def test_cos():
    assert calc.cos(0) == 1

def test_sqrt():
    assert calc.sqrt(25) == 5
    assert calc.sqrt(0) == 0
    with pytest.raises(ValueError):
        calc.sqrt(-1)

def test_percentage():
    assert calc.percentage(20, 50) == 10
    assert calc.percentage(0, 100) == 0
