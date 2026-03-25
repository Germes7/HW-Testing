import pytest

from functions import *

def test_calculate_sum_zero_value():

    assert calculate_sum(0) == "Введен ноль"

def test_calculate_sum_negative_value():

    assert calculate_sum(-1) == "Введено отрицательное число"

def test_calculate_sum_positive_value():

    assert calculate_sum(4) == 10

def test_calculate_sum_empty_value():

    assert calculate_sum("") == "Пустота!"

def test_calculate_sum_string_only_spaces():

    assert calculate_sum("   ") == "Введена пустая строка"

def test_calculate_sum_float_value():

    assert calculate_sum(5.2) == "Введено не целое число"

def test_calculate_sum_symbol():

    assert calculate_sum("+") == "Введен символ"

def test_calculate_sum_one():

    assert calculate_sum(1) == 1, "Введено число 1"

def test_calculate_sum_none_value():

    assert calculate_sum(None) == "Некорректное введение"


def test_count_words_empty_string():
    assert count_words("") == 0, "Пустая строка"

def test_count_words_one_value():
    assert count_words("abc") == 1, "Введено одно слово либо символ"

def test_count_words_one_space():
    assert count_words("   ") == 0, "Введены одни пробелы"

def test_count_words_not_strig():
    assert count_words(5)