from src.app_errors import AppError

def parse_int(text: str) -> int:
    """
    Выделение целого неотрицательного числа из воода пользователя
    :param text: Строка, введенная пользователем
    :return: Целое неотрицательное число
    """
    input = text.split()
    if len(input) < 2:
        raise AppError('Вы не ввели числовой аргумент')
    if len(input) > 2:
        raise AppError('Слишком много аргументов')
    text = input[1]
    try:
        print(int(text.strip()))
        num = int(text.strip())
    except Exception:
        raise AppError(f'Аргументом должно быть целое неторицательное число, вы ввели: {text.strip()}')
    if num < 0:
        raise AppError(f'Аргументом должно быть целое неторицательное число, вы ввели: {text.strip()}')
    return num