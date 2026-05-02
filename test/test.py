import pytest
from add import sum_numbers
from subract import subtract_numbers


# Addition tests
def test_addition_positive_numbers():
    """Test addition of two positive numbers"""
    assert sum_numbers(5, 3) == 8


def test_addition_negative_numbers():
    """Test addition of two negative numbers"""
    assert sum_numbers(-5, -3) == -8


def test_addition_mixed_numbers():
    """Test addition of positive and negative numbers"""
    assert sum_numbers(10, -5) == 5


def test_addition_with_zero():
    """Test addition with zero"""
    assert sum_numbers(5, 0) == 5
    assert sum_numbers(0, 0) == 0


def test_addition_float_numbers():
    """Test addition of float numbers"""
    assert sum_numbers(2.5, 3.5) == pytest.approx(6.0)


def test_addition_large_numbers():
    """Test addition of large numbers"""
    assert sum_numbers(1000000, 2000000) == 3000000


# Subtraction tests
def test_subtraction_positive_numbers():
    """Test subtraction of two positive numbers"""
    assert subtract_numbers(10, 3) == 7


def test_subtraction_negative_numbers():
    """Test subtraction of two negative numbers"""
    assert subtract_numbers(-10, -3) == -7


def test_subtraction_mixed_numbers():
    """Test subtraction with mixed positive and negative numbers"""
    assert subtract_numbers(10, -5) == 15


def test_subtraction_with_zero():
    """Test subtraction with zero"""
    assert subtract_numbers(5, 0) == 5
    assert subtract_numbers(0, 5) == -5
    assert subtract_numbers(0, 0) == 0


def test_subtraction_float_numbers():
    """Test subtraction of float numbers"""
    assert subtract_numbers(5.5, 2.5) == pytest.approx(3.0)


def test_subtraction_large_numbers():
    """Test subtraction of large numbers"""
    assert subtract_numbers(5000000, 2000000) == 3000000
