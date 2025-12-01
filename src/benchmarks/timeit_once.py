import time
from typing import Callable

def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Измеряет время выполнения функции один раз
    :param func: Функция для измерения
    :param *args: Позиционные аргументы
    :param **kwargs: Именованные аргументы
    :returns: Время выполнения в секундах
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time, result