def factorial(n: int) -> int:
    """
    Вычисление факториала циклом
    :param n: Число, факториал которого нужно найти
    :return: Факториал числа
    """
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def factorial_recursive(n: int) -> int:
    """
    Рекурсивное вычисление факториала
    :param n: Число, факториал которого нужно найти
    :return: Факториал числа
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)