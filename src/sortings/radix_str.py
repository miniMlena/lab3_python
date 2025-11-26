from typing import Callable, Any
from src.app_errors import AppError

def radix_sort_str(arr: list[Any], key: Callable[[Any], Any] | None = None) -> list[Any]:
    """
    Поразрядная сортировка строк (поддерживает только символы ASCII)
    :param arr: Список, который нужно отсортировать
    :param key: Ключ, по которому будет происходить сортировка
    :param base: Основание системы счисления
    :return: Возвращает отсортированный список
    """
    if not arr:
        return arr

    pairs = []
    for a in arr:
        if key is not None:
            try:
                sort_value = key(a)
            except Exception:
                raise AppError(f"Нельзя применить указанный ключ к элементу: {"'" + a + "'" if type(a) is str else a}")
        else:
            sort_value = a
        pairs.append((a, sort_value))

    for arr_val, key_val in pairs:
        if not isinstance(key_val, str):
            raise AppError(f"Поразрядная сортировка radix_sort_str работает только со строками, вы ввели: {key_val}")

    max_length = max(len(key_val) for _, key_val in pairs) if pairs else 0

    # Базовый набор символов ASCII
    base = 256
    bins = [[] for _ in range(base)]

    for pos in range(max_length - 1, -1, -1):
        for arr_val, key_val in pairs:
            if pos < len(key_val):
                char_code = ord(key_val[pos])
                if char_code >= base:
                    char_code = base - 1 
            else:
                char_code = 0
            
            bins[char_code].append((arr_val, key_val))

        pairs = []
        for bin_list in bins:
            pairs.extend(bin_list)
            bin_list.clear()

    return [arr_val for arr_val, _ in pairs]


"""print(sorted(text, key=str.lower))
print(radix_sort_str(text, key=keys_dict['len']))"""