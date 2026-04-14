from functions_hw2 import *
import pytest

@pytest.fixture
def clas_temp_1():
    temper = Temperature(7)
    return temper

@pytest.fixture
def clas_temp_2():
    temper = Temperature(-50)
    return temper

@pytest.fixture
def clas_temp_3():
    temper = Temperature(0)
    return temper

def test_temperature_incorrect_type_str():

    with pytest.raises(TypeError):
        Temperature("12")

def test_temperature_incorrect_type_list():

    with pytest.raises(TypeError):
        Temperature([1, 2, 3])

def test_temperature_incorrect_type_typle():

    with pytest.raises(TypeError):
        Temperature((1, 2, 3))

def test_temperature_incorrect_type_dict():

    with pytest.raises(TypeError):
        Temperature({"1": 12})

def test_temperature_incorrect_input_float():

    with pytest.raises(TypeError):
        Temperature(2.5)

def test_to_fahrenheit_1(clas_temp_1):
    assert clas_temp_1.to_fahrenheit() == 44.6

def test_to_fahrenheit_2(clas_temp_2):
    assert clas_temp_2.to_fahrenheit() == -58.0

def test_to_fahrenheit_3(clas_temp_3):
    assert clas_temp_3.to_fahrenheit() == 32.0

def test_to_kelvin_1(clas_temp_1):
    assert clas_temp_1.to_kelvin() == 280.14

def test_to_kelvin_2(clas_temp_2):
    assert clas_temp_2.to_kelvin() == 223.14

def test_to_kelvin_3(clas_temp_3):
    assert clas_temp_3.to_kelvin() == 273.14

def test_is_positive_1(clas_temp_1):
    assert clas_temp_1.is_positive()

def test_is_positive_2(clas_temp_2):
    assert clas_temp_2.is_positive() is False

def test_is_positive_3(clas_temp_3):
    assert clas_temp_3.is_positive() is False

def test_compare(clas_temp_1, clas_temp_3):

    t1 = clas_temp_1
    t2 = clas_temp_3

    assert Temperature.compare(t1, t2) == -1

@pytest.fixture
def book1():
    book = LibraryBook("Вий", "Гоголь Н.В.", 1835)
    return book

@pytest.fixture
def book2():
    book = LibraryBook("Задача трех тел", "Лю Цысинь", 2006)
    return book
def test_incorrect_type_int_title():

    with pytest.raises(TypeError):
        LibraryBook(12, "Блок", 1927)

def test_incorrect_type_int_autor():

    with pytest.raises(TypeError):
        LibraryBook("Кристина", 1, 1983)

def test_incorrect_type_str_year_publication():

    with pytest.raises(TypeError):
        LibraryBook("Кристина", "Стивен Кинг", "сто")

def test_get_title1(book1: LibraryBook):
    assert book1.get_title() == "Вий"

def test_get_title2(book2: LibraryBook):
    assert book2.get_title() == "Задача трех тел"

def test_get_autor1(book1: LibraryBook):
    assert book1.get_autor() == "Гоголь Н.В."

def test_get_autor2(book2: LibraryBook):
    assert book2.get_autor() == "Лю Цысинь"

def test_get_year_publication1(book1: LibraryBook):
    assert book1.get_year_publication() == 1835

def test_get_year_publication2(book2: LibraryBook):
    assert book2.get_year_publication() == 2006

def test_is_old1(book1: LibraryBook):
    assert book1.is_old(2000) is True

def test_is_old2(book2: LibraryBook):
    assert book2.is_old(2000) is not True

def test_age1(book1: LibraryBook):
    assert book1.age(2026) == 191

def test_incorrect_type_str_age():

    with pytest.raises(TypeError):
        LibraryBook.age("сто")

def test_incorrect_type_float_age():

    with pytest.raises(TypeError):
        LibraryBook.age(123.5)
