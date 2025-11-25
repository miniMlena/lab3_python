from src.constants import LIST_RE, SORT_RE, keys_dict, cmps_dict
from src.sortings.sort_errors import SortError

def parse_sort(text):
    parsed_groups = SORT_RE.match(text)

    parsed_list = parsed_groups('list')
    if parsed_list is None:
        raise SortError('Некорректный ввод списка')
    else:
        list = read_list(parsed_list)

    parsed_key = parsed_groups('key')
    if parsed_key not in keys_dict:
        raise SortError(f'Введенный ключ не найден: {parsed_key}')
    else:
        key = keys_dict[parsed_key]

    parsed_cmp = parsed_groups('cmp')
    if parsed_cmp not in cmps_dict:
        raise SortError(f'Введенный компаратор не найден: {parsed_cmp}')
    else:
        cmp = cmps_dict[parsed_cmp]

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

