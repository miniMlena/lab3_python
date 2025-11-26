from typing import TypeVar, Callable, Any
from src.constants import LIST_RE, SORT_RE, keys_dict, cmps_dict
from src.app_errors import AppError

T = TypeVar('T')

def parse_sort(text: str, sort_type: str) -> tuple[list[Any],
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
        if parsed_cmp not in cmps_dict:
            raise AppError(f'Введенный компаратор не найден: {parsed_cmp}')
        else:
            cmp = cmps_dict[parsed_cmp]

    if sort_type == 'rad_int':
        parsed_base = match.group('base')
        if parsed_base:
            try: 
                base = int(parsed_base)
            except ValueError:
                raise AppError(f'Основание системы счисления должно быть целым числом, вы ввели: {parsed_base}')
            return list, key, base


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