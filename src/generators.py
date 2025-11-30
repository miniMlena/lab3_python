import random
from src.app_errors import AppError

def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: int | None = None) -> list[int]:
    """
    Генерирует массив случайных целых чисел
    :param n: Количество элементов
    :param lo: Минимальное значение
    :param hi: Максимальное значение
    :param distinct: Если True, все числа уникальны
    :param seed: Seed для генератора случайных чисел
    :return: Список случайных целых чисел
    """
    if seed is not None:
        random.seed(seed)
    
    if lo > hi:
        raise AppError(f"Правая граница интервала должна быть больше левой, вы ввели: {lo} > {hi}")

    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f"Невозможно сгенерировать {n} уникальных целых чисел в диапазоне [{lo}, {hi}]")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed: int | None = None) -> list[int]:
    """
    Генерирует почти отсортированный массив
    :param n: Количество элементов
    :param swaps: Количество случайных обменов для нарушения порядка
    :param seed: Seed для генератора случайных чисел
    :returns: Почти отсортированный список
    """
    if seed is not None:
        random.seed(seed)

    arr = list(range(n))

    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def many_duplicates(n: int, k_unique: int = 5, *, seed: int | None = None) -> list[int]:
    """
    Генерирует массив с большим количеством дубликатов
    :param n: Количество элементов
    :param k_unique: Количество уникальных значений
    :param seed: Seed для генератора случайных чисел
    :returns: Список с множеством дубликатов
    """
    if seed is not None:
        random.seed(seed)

    unique_values = list(range(k_unique))

    return [random.choice(unique_values) for _ in range(n)]

def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует обратно отсортированный массив
    :param n: Количество элементов
    :returns: Обратно отсортированный список
    """
    return list(range(n - 1, -1, -1))

def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed: int | None = None) -> list[float]:
    """
    Генерирует массив случайных вещественных чисел
    :param n: Количество элементов
    :param lo: Минимальное значение
    :param hi: Максимальное значение
    :param seed: Seed для генератора случайных чисел
    :returns: Список случайных вещественных чисел
    """
    if seed is not None:
        random.seed(seed)
    
    if lo > hi:
        raise AppError(f"Правая граница интервала должна быть больше левой, вы ввели: {lo} > {hi}")

    return [random.uniform(lo, hi) for _ in range(n)]

def generate_list(text: str) -> list[int | float]:
    """
    Генерирует список указанного типа
    :param text: Строка, описывающая тип генератора и аргументы
    :return: Сгенерированный список
    """
    text = text.strip()
    parts = text.split()
    gen_type = parts.pop(0)

    try:
        amount = int(parts.pop(0))
        if amount <= 0:
            raise AppError(f"Количество элементов в списке должно быть положительным числом, вы ввели: {amount}")

        if gen_type == 'rand_int_array':
            arg_lo, arg_hi = int(parts[0]), int(parts[1])
            return rand_int_array(amount, arg_lo, arg_hi)
        elif gen_type == 'nearly_sorted':
            arg_swap = int(parts[0])
            if arg_swap <= 0:
                raise AppError(f"Количество перестановок должно быть положительным числом, вы ввели: {arg_swap}")
            return nearly_sorted(amount, arg_swap)
        elif gen_type == 'many_duplicates':
            arg_uniq = int(parts[0])
            if arg_uniq <= 0:
                raise AppError(f"Количество уникальных элементов должно быть положительным числом, вы ввели: {arg_uniq}")
            return many_duplicates(amount, arg_uniq)
        elif gen_type == 'reverse_sorted':
            return reverse_sorted(amount)
        elif gen_type == 'rand_float_array':
            arg_lo, arg_hi = float(parts[0]), float(parts[1])
            return rand_float_array(amount, arg_lo, arg_hi)
        else:
            raise AppError("Некорректный ввод генератора")
    except IndexError:
        raise AppError("Недостаточно аргументов для генерации списка")