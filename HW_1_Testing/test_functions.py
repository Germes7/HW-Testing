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

def test_count_words_not_string():
    assert count_words(5) == "Ошибка: введена не строка"

def test_count_words_tab_space():
    assert count_words("Hello\tworld\nhello\thello\nworld") == 5

def test_count_words_input_non():
    assert count_words(None) == "Ошибка: введена не строка", "Введен None"

def test_count_words_input_float():
    assert count_words(3.1415) == "Ошибка: введена не строка", "Введен float"

def test_count_words_input_list():
    assert count_words([]) == "Ошибка: введена не строка", "Введен список"

def test_count_words_input_tuple():
    assert count_words(()) == "Ошибка: введена не строка", "Введен кортеж"


def test_is_number_empty_string():
    assert is_number("") == "Ошибка", "Введена пустая строка"

def test_is_number_double_string():
    assert is_number("1 2") == "Ошибка", "Введены два числа"

def test_is_number_no_number_string():
    assert is_number("gh") == "Ошибка", "Введено строчно не число"

def test_is_number_input_symbol():
    assert is_number("+") == "Ошибка", "Введен символ"

def test_is_number_input_string_symbol_and_number():
    assert is_number("+ 12")  == "Ошибка", "Введены символ и число"

def test_is_number_input_number():
    assert is_number(1)  == "Ошибка", "Введено число"

def test_is_number_list():
    assert is_number([]) == "Ошибка", "Введен список"

def test_is_number_input_string_float():
    assert is_number("2.71") == "Ошибка", "Введен float"