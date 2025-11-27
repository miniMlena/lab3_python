from typing import TypeVar, Callable, Any
from src.app_errors import AppError
from src.constants import SORT_RE, KEYS_DICT, CMPS_DICT
from src.read_list import read_list

T = TypeVar('T')

def parse_sort(text: str, sort_type: str | None = None) -> tuple[list[Any],
               Callable[[Any], Any] | None, Callable[[T, T], int] | None]:
    """
    Выделение списка и параметров из строки, введенной пользователем
    :param text: Строка, введенная пользователем
    :param sort_type: Тип сортировки
    :return: Кортеж, содержащий список и все параметры для сортировки
    """
    input = text.split(maxsplit=1)
    if len(input) < 2:
        raise AppError('Недостаточно аргументов')
    
    text = input[1]
    match = SORT_RE.match(text)

    parsed_list = match.group('list')
    if parsed_list is None:
        raise AppError('Некорректный ввод списка')
    else:
        list = read_list(parsed_list)

    key = None
    parsed_key = match.group('key')
    if parsed_key:
        if parsed_key not in KEYS_DICT:
            raise AppError(f'Введенный ключ не найден: {parsed_key}')
        else:
            key = KEYS_DICT[parsed_key]

    cmp = None
    parsed_cmp = match.group('cmp')
    if parsed_cmp:
        if sort_type not in ('bubble', 'quick', 'heap'):
            raise AppError('Эта сортировка не поддерживает компараторы')
        if parsed_cmp not in CMPS_DICT:
            raise AppError(f'Введенный компаратор не найден: {parsed_cmp}')
        else:
            cmp = CMPS_DICT[parsed_cmp]

    parsed_base = match.group('base')
    if parsed_base:
        if sort_type != 'rad_int':
            raise AppError('Эта сортировка не поддерживает параметр base')
        try:
            base = int(parsed_base)
        except Exception:
            raise AppError(f'Основание системы счисления должно быть целым числом, вы ввели: {parsed_base}') 
        if base <= 1:
            raise AppError("Основание системы счисления должно быть больше 1")
        return list, key, base

    parsed_buckets = match.group('buckets')
    if parsed_buckets:
        if sort_type != 'bucket':
            raise AppError("Эта сортировка не поддерживает параметр buckets")
        try:
            buckets = int(parsed_buckets)
        except Exception:
            raise AppError("Параметр buckets должен быть целым положительным числом")
        if buckets < 1:
            raise AppError("Параметр buckets должен быть целым положительным числом")
        return list, key, buckets

    if sort_type in ('count', 'rad_int' 'rad_str', 'bucket'):
        return list, key
    elif sort_type in ('bubble', 'quick', 'heap'):
        return list, key, cmp