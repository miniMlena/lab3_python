from typing import Any
from src.app_errors import AppError
from src.constants import LIST_RE

def read_list(parsed_list) -> list[Any]:
    """
    Чтение списка из строки
    :param parsed_list: Строка, содержащая список
    :return: Прочитанный список
    """
    parsed_list = parsed_list.strip()

    if not parsed_list.startswith('[') or not parsed_list.endswith(']'):
        raise AppError('Некорректный ввод списка')
    
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