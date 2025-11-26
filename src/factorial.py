from src.app_errors import AppError

def factorial_iter(n: int) -> int:  #максиму 1558
    """
    Вычисление факториала циклом
    :param n: Число, факториал которого нужно найти
    :return: Факториал числа
    """
    if n > 1550:
        raise AppError('Команда factorial_iter работает с числами не более 1550')
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def factorial_recursive(n: int) -> int: # максимум 999
    """
    Рекурсивное вычисление факториала
    :param n: Число, факториал которого нужно найти
    :return: Факториал числа
    """
    if n > 999:
        raise AppError('Команда factorial_rec работает с числами не более 999. Попробуйте factorial_iter :)')
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)