from typing import TypeVar, Callable, Any
from src.sortings.keys_comps import build_compare
from src.app_errors import AppError

T = TypeVar('T')

def quick_sort(arr: list[Any], key: Callable[[Any], Any] | None = None,
               cmp: Callable[[T, T], int] | None = None) -> list[Any]:
    """
    Быстрая сортировка
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param cmp: Компаратор, котрый будет использован при сортировке
    :return: Возвращает отсортированный список
    """
    compare = build_compare(key, cmp)
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            try:
                if compare(arr[j], pivot) <= 0:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            except Exception:
                raise AppError(f'Нельзя сравнить элементы по указанным правилам: {arr[j]} и {pivot}. Ошибка в ключе или компараторе')
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def _quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            _quicksort(low, pi - 1)
            _quicksort(pi + 1, high)

    _quicksort(0, len(arr) - 1)

    return arr