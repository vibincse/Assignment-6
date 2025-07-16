# test_fibonacci.py
import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fibonacci import Fibonacci


def test_non_integer_input_raises_value_error():
    with pytest.raises(ValueError):
        list(Fibonacci("not_an_integer"))

def test_fibonacci_zero():
    assert list(Fibonacci(0)) == [0]


def test_fibonacci_one():
    assert list(Fibonacci(1)) == [0, 1]


def test_fibonacci_four():
    assert list(Fibonacci(4)) == [0, 1, 1, 2, 3]
