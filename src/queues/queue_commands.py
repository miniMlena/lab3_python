from src.queues.queue_class import Queue
from src.app_errors import AppError
from src.read_list import read_list

queues = {}

def create_queue(text: str) -> None:
    """
    Создает новую очередь
    :param text: Строка, введенная пользователем
    :return: Данная функция ничего не возвращает
    """
    parts = text.split(maxsplit=2)
    
    if len(parts) < 2:
        raise AppError("Недостаточно аргументов")

    queue_name = parts[1]
    if queue_name in queues:
        raise AppError(f"Очередь {queue_name} уже существует")
    
    queues[queue_name] = Queue()

    if len(parts) > 2:
        list = parts[2].strip()
        elements = read_list(list)
        
        for elem in elements:
            queues[queue_name].enqueue(elem)
    
    print(f"Очередь {queue_name} создана")

def show_queue(text: str) -> None:
    """
    Показывает очередь или все очереди
    :param text: Строка, введенная пользователем
    :return: Данная функция ничего не возвращает
    """
    parts = text.split(maxsplit=1)
    arg = None
    if len(parts) > 1:
        arg = parts[1]

    if not arg:
        raise AppError("Недостаточно аргументов")
    
    if arg == "all":
        if not queues:
            print("Пока нет ни одной очереди, используйте create для создания")
        else:
            result = ["Все очереди:"]
            for name, queue in queues.items():
                result.append(f"{name}: {format_queue(queue)}")
            print('\n'.join(result))
    else:
        queue_name = arg
        if queue_name not in queues:
            raise AppError(f"Очередь не найдена: {queue_name}")
        print(f"Очередь {queue_name}: {format_queue(queues[queue_name])}")

def delete_queue(text: str) -> None:
    """
    Удаляет очередь
    :param text: Строка, введенная пользователем
    :return: Данная функция ничего не возвращает
    """
    parts = text.split(maxsplit=1)
    arg = None
    if len(parts) > 1:
        arg = parts[1]

    if not arg:
        raise AppError("Недостаточно аргументов")
    
    queue_name = arg
    if queue_name not in queues:
        raise AppError(f"Очередь не найдена: {queue_name}")
    
    del queues[queue_name]
    print(f"Очередь {queue_name} удалена")

def queue_operation(queue_name: str, operation: str, text: str) -> None:
    """
    Выполняет операцию над очередью
    :param queue_name: Название очереди
    :param operation: Название операции
    :param text: Строка, введенная пользователем
    :return: Данная функция ничего не возвращает
    """
    parts = text.split(maxsplit=2)
    if len(parts) > 2:
        arg = parts[2].strip()
    else:
        arg = None
    
    if queue_name not in queues:
        raise AppError(f"Очередь не найдена: {queue_name}")
    
    queue = queues[queue_name]
    
    if operation == "add":
        if not arg:
            raise AppError("Недостаточно аргументов")
        
        if arg.startswith('"') and arg.endswith('"'):
            value = arg[1:-1]
        elif arg.startswith("'") and arg.endswith("'"):
            value = arg[1:-1]
        elif arg.isdigit() or (arg.startswith('-') and arg[1:].isdigit()):
            value = int(arg)
        else:
            try:
                value = float(arg)
            except ValueError:
                value = arg
        
        queue.enqueue(value)
        print(f"Элемент {value} добавлен в {queue_name}: {format_queue(queue)}")
    
    elif operation == "remove":
        value = queue.dequeue()
        print(f"Элемент {value} удален из {queue_name}: {format_queue(queue)}")
    
    elif operation == "front":
        value = queue.front()
        print(f"Первый элемент в очереди {queue_name}: {value}")
    
    elif operation == "size":
        print(f"Размер {queue_name}: {len(queue)}")
    
    elif operation == "is_empty":
        print(f"Очередь {queue_name} {'' if queue.is_empty() else 'не '}пуста")
    
    else:
        print(f"Операция не найдена: {operation}")

def format_queue(queue: Queue) -> str:
    """
    Форматирует очередь для вывода
    :param queue: Очередь, которую нужно подготовить для вывода
    :return: Отформотированная строка
    """
    elements = []
    current = queue.head
    while current:
        elements.append(str(current.value))
        current = current.next
    return "[" + " -> ".join(elements) + "]" if elements else "[]"