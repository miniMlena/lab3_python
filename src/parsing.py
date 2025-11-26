from typing import TypeVar, Callable, Any
from src.constants import LIST_RE, SORT_RE, keys_dict, cmps_dict
from src.app_errors import AppError

T = TypeVar('T')

def parse_int(text: str) -> int:
    input = text.split(maxsplit=1)
    if len(input) < 2:
        raise AppError('Вы не ввели числовой аргумент')
    text = input[1]
    try:
        print(int(text.strip()))
        num = int(text.strip())
    except Exception:
        raise AppError(f'Эта функция принимает целые неторицательные числа, вы ввели: {text.strip()}')
    if num < 0:
        raise AppError(f'Эта функция принимает целые неторицательные числа, вы ввели: {text.strip()}')
    return num

def parse_sort(text: str, sort_type: str | None = None) -> tuple[list[Any],
    Callable[[Any], Any] | None, Callable[[T, T], int] | None]:
    """
    
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
        if parsed_key not in keys_dict:
            raise AppError(f'Введенный ключ не найден: {parsed_key}')
        else:
            key = keys_dict[parsed_key]

    cmp = None
    parsed_cmp = match.group('cmp')
    if parsed_cmp:
        if sort_type not in ('bubble', 'quick', 'heap'):
            raise AppError('Эта сортировка не поддерживает компараторы')
        if parsed_cmp not in cmps_dict:
            raise AppError(f'Введенный компаратор не найден: {parsed_cmp}')
        else:
            cmp = cmps_dict[parsed_cmp]

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
    else:
        return list, key, cmp


def read_list(parsed_list):
    parsed_list = parsed_list.strip()

    content = parsed_list[1:-1].strip()
    
    if not content:
        return []
    
    items = LIST_RE.findall(content)
    result = []
    
    for item in items:
        item = item.strip()
        if not item:
            continue

        if item.startswith('"') and item.endswith('"'):
            result.append(item[1:-1])
        elif item.startswith("'") and item.endswith("'"):
            result.append(item[1:-1])
        elif item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
            result.append(int(item))
        else:
            try:
                result.append(float(item))
            except ValueError:
                result.append(item)

    return result

'''from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
text = input()
print(quick_sort(*parse_sort(text)))
print(bubble_sort(*parse_sort(text)))'''

'''from src.sortings.radix_str import radix_sort_str
text="radix_sort_str ['abc', \"zxc\", 'hg', 1.5, \"\", \"33.3\" 'ab']"
print(radix_sort_str(*parse_sort(text, 'rad_str')))'''