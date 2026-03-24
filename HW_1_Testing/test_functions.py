import pytest

from functions import calculate_sum

def test_calculate_sum_zero_value():

    with pytest.raises(ValueError):
        calculate_sum(0)

def test_calculate_sum_negative_value():

    with pytest.raises(ValueError):
        calculate_sum(-1)

def test_calculate_sum_positive_value():
    assert calculate_sum(4) == 10

def test_calculate_sum_empty_value():
    with pytest.raises(ValueError):
        calculate_sum("")

def test_calculate_sum_string_value():
    with pytest.raises(ValueError):
        calculate_sum("n")

def test_calculate_sum_float_value():
    with pytest.raises(ValueError):
        calculate_sum(5.2)

def test_calculate_sum_symbol():
    with pytest.raises(ValueError):
        calculate_sum("+")
