from typing import TypeVar, Callable, Any
from src.app_errors import AppError

T = TypeVar('T')

def count_sort(arr: list[T], key: Callable[[T], Any] | None = None) -> list[T]:
    if not arr:
        return arr

    pairs = []
    for arr_value in arr:
        if key is not None:
            try:
                key_value = key(arr_value)
            except Exception as e:
                raise AppError(f"Нельзя применить ключ к элементу {arr_value}: {e}")
        else:
            key_value = arr_value
        pairs.append((arr_value, key_value))

    for arr_value, key_value in pairs:
        if not isinstance(key_value, int):
            raise AppError(f"Сортировка счетом работает только с целыми числами, вы ввели: {key_value}")

    values = [key_value for _, key_value in pairs]
    min_val = min(values)
    max_val = max(values)

    range_size = max_val - min_val + 1

    count = [0] * range_size

    for arr_value, key_value in pairs:
        index = key_value - min_val  # Смещаем все элементы в неотрицательную область, позволяет обрабатывать отрицательные числа
        count[index] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [None] * len(arr)
    
    # Размещаем элементы в обратном порядке, т.к. иначе порядок элементов с
    # одинаковым key_value поменяется по сравнению с их порядком в исходном списке
    for item, value in reversed(pairs):
        index = value - min_val
        pos = count[index] - 1
        output[pos] = item
        count[index] -= 1
    
    return output
