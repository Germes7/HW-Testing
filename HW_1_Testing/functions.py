# 1. Функция calculate_sum(n), возвращающая сумму чисел от 1 до n.

def calculate_sum(n):

    if not isinstance(n, int):
        if n is None: return "Некорректное введение"
        if isinstance(n, float): return "Введено не целое число"
        if isinstance(n, str):

            if n == "": return "Пустота!"

            elif n.strip() == "": return "Введена пустая строка"

            else:
                return "Введен символ"

        return "Некорректное введение"

    if n == 0: return "Введен ноль"
    if n < 0: return "Введено отрицательное число"

    summator = 0
    for i in range(1, n + 1):

        summator += i

    return summator


# 2. Функция count_words(line), возвращающая количество слов в строке (слова разделены пробелами).

def count_words(line):

    if not isinstance(line, str):
        return "Ошибка: введена не строка"

    return len(line.strip().split())


# 3. Функция is_number(string), которая проверяет, что переданная строка это целое число.

def is_number(string):

    if not isinstance(string, str) or (string, None):
        return "Ошибка"

    if string.isdigit(): return string


# 4. Функция unique(lst), возвращающая список уникальных элементов в переданном списке.

def unique(lst):

    if not isinstance(lst, list):
        return "Ошибка"

    if not lst: return []

    if len(lst) == 1: return lst

    uniq_lst = []
    for i in lst:
        if i not in uniq_lst:
            uniq_lst.append(i)

    return uniq_lst