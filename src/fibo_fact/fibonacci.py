import functools
from src.app_errors import AppError

def fibo_iter(n: int) -> int: #максимум 20577
    """
    Вычисление числа Фибоначчи циклом
    :param n: Номер числа Фибоначчи
    :return: Величина числа Фибоначчи
    """
    if n > 20500:
        raise AppError('Команда fibonacci_iter работает с числами не более 20 500')
    f1, f2 = 0, 1
    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2

@functools.cache
def fibo_recursive(n: int) -> int: #максимум 1996
    """
    Вычисление числа Фибоначчи рекурсией
    :param n: Номер числа Фибоначчи
    :return: Величина числа Фибоначчи
    """
    if n > 1900:
        raise AppError('Команда fibonacci_rec работает с числами не более 1900. Попробуйте fibonacci_iter :)')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 2) + fibo_recursive(n - 1)