from typing import Callable, Any
from src.app_errors import AppError

def radix_sort_int(arr: list[Any], key: Callable[[Any], Any] | None = None, base: int = 10) -> list[Any]:
    """
    Поразрядная сортировка целых неотрицательных чисел
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param base: Основание системы счисления
    :return: Возвращает отсортированный список
    """
    if not arr:
        return arr
    
    # Создаем пары (элемент, значение_для_сортировки)
    pairs = []
    for a in arr:
        if key is not None:
            try:
                sort_value = key(a)
            except Exception:
                raise AppError(f"Нельзя применить указанный ключ к элементу: {"'" + a + "'" if type(a) is str else a}")
        else:
            sort_value = a
        pairs.append((a, sort_value))

    for arr_val, key_val in pairs:
        if not (isinstance(key_val, int) and key_val >= 0):
            raise AppError(f"Поразрядная сортировка radix_sort_int работает только с целыми неотрицаительыми числами, вы ввели: {"'" + key_val + "'" if type(key_val) is str else key_val}")

    max_digits = max([len(str(key_val)) for arr_val, key_val in pairs])

    bins = [[] for _ in range(base)]
    
    for i in range(max_digits):
        for arr_val, key_val in pairs:
            digit = (key_val // (base ** i)) % base
            bins[digit].append((arr_val, key_val))

        pairs = []
        for bin_list in bins:
            pairs.extend(bin_list)

        bins = [[] for _ in range(base)]

    arr = []
    for arr_val, key_val in pairs:
        arr.append(arr_val)
    
    return arr

#print(radix_sort_int([1, 40, 22, 5], None))