from typing import TypeVar, Callable, Any
from src.app_errors import AppError
from src.constants import LIST_SORT_RE, KEY_RE, CMP_RE, BASE_RE, BUCKETS_RE, KEYS_DICT, CMPS_DICT
from src.read_list import read_list
from src.generators import generate_list
import re

T = TypeVar('T')

def parse_sort(text: str) -> tuple[list[Any], Callable[[Any], Any] | None, Callable[[T, T], int] | None]:
    """
    Выделение списка и параметров из строки, введенной пользователем
    :param text: Строка, введенная пользователем
    :return: Кортеж, содержащий список и все параметры для сортировки
    """
    input = text.split(maxsplit=1)
    if len(input) < 2:
        raise AppError('Недостаточно аргументов')
    
    sort_type = input[0]
    text = input[1]

    parsed_lists = re.findall(LIST_SORT_RE, text)
    
    if parsed_lists and len(parsed_lists) > 1:
        raise AppError("Можно ввести только 1 список для сортировки")
    
    if parsed_lists is None or parsed_lists == []:
        raise AppError('Некорректный ввод списка')
    else:
        parsed_list = parsed_lists[0]
        if parsed_list.startswith('['):
            list = read_list(parsed_list)
        else:
            list = generate_list(parsed_list)
            print('Сгенерированный список:', list)

    key = None
    parsed_keys = re.findall(KEY_RE, text)
    if parsed_keys and len(parsed_keys) > 1:
        raise AppError("Можно ввести только 1 ключ для сортировки")

    if parsed_keys:
        parsed_key = parsed_keys[0]
        if parsed_key not in KEYS_DICT:
            raise AppError(f'Введенный ключ не найден: {parsed_key}')
        else:
            key = KEYS_DICT[parsed_key]

    cmp = None
    parsed_cmps = re.findall(CMP_RE, text)
    if parsed_cmps and len(parsed_cmps) > 1:
        raise AppError("Можно ввести только 1 компаратор для сортировки")

    if parsed_cmps:
        parsed_cmp = parsed_cmps[0]
        if sort_type not in ('bubble_sort', 'quick_sort', 'heap_sort'):
            raise AppError('Эта сортировка не поддерживает компараторы')
        if parsed_cmp not in CMPS_DICT:
            raise AppError(f'Введенный компаратор не найден: {parsed_cmp}')
        else:
            cmp = CMPS_DICT[parsed_cmp]

    parsed_bases = re.findall(BASE_RE, text)
    if parsed_bases and len(parsed_bases) > 1:
        raise AppError("Можно ввести только одно основание СС для сортировки")
    
    if parsed_bases:
        parsed_base = parsed_bases[0]
        if sort_type != 'radix_sort_int':
            raise AppError('Эта сортировка не поддерживает параметр base')
        try:
            base = int(parsed_base)
        except Exception:
            raise AppError(f'Основание системы счисления должно быть целым числом, вы ввели: {parsed_base}') 
        if base <= 1:
            raise AppError("Основание системы счисления должно быть больше 1")
        return list, key, base

    parsed_bucketsss = re.findall(BUCKETS_RE, text)
    if parsed_bucketsss and len(parsed_bucketsss) > 1:
        raise AppError("Можно ввести только 1 значение параметра buckets для сортировки")

    if parsed_bucketsss:
        parsed_buckets = parsed_bucketsss[0]
        if sort_type != 'bucket_sort':
            raise AppError("Эта сортировка не поддерживает параметр buckets")
        try:
            buckets = int(parsed_buckets)
        except Exception:
            raise AppError("Параметр buckets должен быть целым положительным числом")
        if buckets < 1:
            raise AppError("Параметр buckets должен быть целым положительным числом")
        return list, key, buckets

    if sort_type in ('counting_sort', 'radix_sort_int', 'radix_sort_str', 'bucket_sort'):
        return list, key
    elif sort_type in ('bubble_sort', 'quick_sort', 'heap_sort'):
        return list, key, cmp