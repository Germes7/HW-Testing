# Функция calculate_sum(n), возвращающую сумму чисел от 1 до n.

def calculate_sum(n):

    if not isinstance(n, int) or n < 1: raise ValueError("Введите целое положительное число")

    sum = 0
    for iter in range(1, n + 1):

        sum += iter

    return sum

