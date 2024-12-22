# test_main.py
import pytest
from main import add_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5
    assert subtract_numbers(0, 5) == -5
    assert subtract_numbers(-5, -5) == 0

if __name__ == "__main__":
    pytest.main()
