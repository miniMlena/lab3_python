from typing import Callable, Any, TypeVar
from src.sortings.keys_comps import build_compare
from src.app_errors import AppError

T = TypeVar('T')

def heap_sort(arr: list[Any], key: Callable[[Any], Any] | None = None,
                      cmp: Callable[[T, T], int] | None = None) -> list[Any]:
    """
    
    """
    if not arr:
        return arr

    compare = build_compare(key, cmp)
    n = len(arr)
    
    def heapify(n: int, i: int):
        """Просеивание элемента вниз"""
        max_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        try:
            if left < n and compare(arr[left], arr[max_index]) > 0:
                max_index = left
        except Exception:
                raise AppError(f'Нельзя сравнить элементы по указанным правилам: {arr[left]} и {arr[max_index]}. Ошибка в ключе или компараторе')
            
        try:
            if right < n and compare(arr[right], arr[max_index]) > 0:
                max_index = right
        except Exception:
            raise AppError(f'Нельзя сравнить элементы по указанным правилам: {arr[right]} и {arr[max_index]}. Ошибка в ключе или компараторе')

        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]
            heapify(n, max_index)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    
    return arr