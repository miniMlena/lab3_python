from typing import Callable, Any
from src.app_errors import AppError

def count_sort(arr: list[Any], key: Callable[[Any], int] | None = None) -> list[Any]:
    """
    Сортировка счётом
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :return: Отсортированный список
    """
    if not arr:
        return arr

    keys = []
    if key is not None:
        for a in arr:
            try:
                keys.append(key(a))
            except Exception:
                raise AppError(f"Нельзя применить ключ к элементу {"'" + a + "'" if type(a) is str else a}")
    else:
        keys = arr

    for k in keys:
        if not isinstance(k, int):
            raise AppError(f"Сортировка счетом работает только с целыми числами, вы ввели: {"'" + k + "'" if type(k) is str else k}")

    min_val = min(keys)
    max_val = max(keys)

    range_size = max_val - min_val + 1

    count = [0] * range_size
    for k in keys:  # Смещаем все элементы в неотрицательную область, позволяет обрабатывать отрицательные числа
        count[k - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [None] * len(arr)
    
    # Размещаем элементы в обратном порядке, т.к. иначе порядок элементов с
    # одинаковым key_value поменяется по сравнению с их порядком в исходном списке
    for i in range(len(arr) - 1, -1, -1):
        k = keys[i]
        idx = k - min_val
        pos = count[idx] - 1
        output[pos] = arr[i]
        count[idx] -= 1
    
    return output