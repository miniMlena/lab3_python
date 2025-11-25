from typing import TypeVar, Callable, Any
from keys_comps import build_compare

T = TypeVar('T')

def quick_sort(arr: list[T], key: Callable[[T], Any] | None = None,
              cmp: Callable[[T, T], int] | None = None) -> list[T]:
    """
    Быстрая сортировка
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param cmp: Компаратор, котрый будет использован при сортировке
    :return: Возвращает отсортированный список
    """
    compare = build_compare(key, cmp)
    
    def _quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            _quicksort(low, pi - 1)
            _quicksort(pi + 1, high)
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if compare(arr[j], pivot) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    _quicksort(0, len(arr) - 1)

    return arr

"""a = [1, 58, 34, 102]
print(quick_sort(a))"""