from typing import TypeVar, Callable, Any

T = TypeVar('T')

def radix_sort_str(arr: list[T], key: Callable[[T], Any] | None = None) -> list[T]:
    """
    Поразрядная сортировка строк (поддерживает символы ASCII)
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param base: Основание системы счисления
    :return: Возвращает отсортированный список
    """
    if not arr:
        return arr

    if key is not None:
        strings = [key(x) for x in arr]
    else:
        strings = arr

    if not all(isinstance(x, str) for x in strings):
        raise ValueError("""Поразрядная сортировка radix_str работает только со строками.
                         Возможно вы хотели использовать radix_int
                         для порязрядной сортировки целых чисел?""")
    
    

#print(radix_sort_int([101, 23, 56, 2, 0, 90], key=lambda x: x%5))
