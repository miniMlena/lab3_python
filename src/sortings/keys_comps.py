from typing import TypeVar, Any, Callable

T = TypeVar('T')

def build_compare(key: Callable[[Any], Any] | None = None, 
                  cmp: Callable[[T, T], int] | None = None) -> Callable[[T, T], int]:
    """
    Создает функцию сравнения с учетом ключа и компаратора для функций сортировки
    :param key: Ключ для сортироовки
    :param cmp: Компаратор для сортировки
    :return: Функция сравнения с учетом ключа и компаратора
    """
    if cmp is None and key is None:
        return lambda x, y: (x > y) - (x < y) # Сортировка значений по возрастанию (по умолчанию)
    elif cmp is not None and key is None:
        return cmp
    elif cmp is None and key is not None:
        return lambda x, y: (key(x) > key(y)) - (key(x) < key(y))
    else:
        return lambda x, y: cmp(key(x), key(y))