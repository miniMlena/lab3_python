from typing import TypeVar, Callable, Any
from src.sortings.keys_comps import build_compare
from src.app_errors import AppError

T = TypeVar('T')

def bubble_sort(arr: list[Any], key: Callable[[Any], Any] | None = None,
                cmp: Callable[[T, T], int] | None = None) -> list[Any]:
    """
    Сортировка пузырьком
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param cmp: Компаратор, котрый будет использован при сортировке
    :return: Возвращает отсортированный список
    """
    compare = build_compare(key, cmp)

    n = len(arr)
    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            try:
                if compare(arr[j], arr[j + 1]) > 0:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            except Exception:
                raise AppError(f'Нельзя сравнить элементы по указанным правилам: {arr[j]} и {arr[j + 1]}. Ошибка в ключе или компараторе')
        if not swapped:
            break

    return arr