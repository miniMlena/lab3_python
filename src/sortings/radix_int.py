from typing import TypeVar, Callable, Any
from src.sortings.sort_errors import SortError

T = TypeVar('T')

def radix_sort_int(arr: list[T], key: Callable[[T], Any] | None = None, base: int = 10) -> list[T]:
    """
    Поразрядная сортировка целых неотрицательных чисел
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param base: Основание системы счисления
    :return: Возвращает отсортированный список
    """
    if not arr:
        return arr
    
    if base <= 1:
        raise ValueError("Основание системы счисления должно быть больше 1")
    
    # Создаем пары (элемент, значение_для_сортировки)
    pairs = []
    for a in arr:
        if key is not None:
            try:
                sort_value = key(a)
            except Exception:
                raise SortError(f"Нельзя применить указанный ключ к элементу: {a}")
        else:
            sort_value = a
        pairs.append((a, sort_value))

    for arr_val, key_val in pairs:
        if not (isinstance(key_val, int) and key_val >= 0):
            raise ValueError(f"""Поразрядная сортировка radix_int работает только с целыми
                             неотрицаительыми числами, вы ввели: {key_val}.
                             \nМожет, вы хотели использовать radix_str
                             для порязрядной сортировки строк?""")

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

print(radix_sort_int([101, '23', 56, 2, 0, 90], key=lambda x: x%5))