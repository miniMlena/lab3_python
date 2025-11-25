from typing import TypeVar, Callable, Any
from src.sortings.keys_comps import build_compare

T = TypeVar('T')

def bubble_sort(arr: list[T], key: Callable[[T], Any] | None = None,
cmp: Callable[[T, T], int] | None = None) -> list[T]:
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
            if compare(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr