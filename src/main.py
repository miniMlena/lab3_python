from src.info import info
from src.sortings.parse_sort import parse_sort
from src.fibo_fact.parse_int import parse_int
from src.fibo_fact.factorial import factorial_iter, factorial_recursive
from src.fibo_fact.fibonacci import fibo_iter, fibo_recursive
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.sortings.radix_int import radix_sort_int
from src.sortings.radix_str import radix_sort_str
from src.sortings.buckets import bucket_sort
from src.sortings.heap import heap_sort
from src.queues.queue_commands import create_queue, delete_queue, show_queue, queue_operation

def main() -> None:
    """
    Точка входа в программу
    :return: Данная функция ничего не возвращает
    """
    print('Добро пожаловать в программу для подсчёта факториалов и чисел Фибоначчи, сортировки списков и работы с очередями! Чтобы узнать о всех доступных командах введите info. Для выхода введите quit')
    
    while (user_input:=input("Введите команду: ")).lower() != "quit":
        
        if not user_input:
            continue

        text = user_input.split()
        command = text[0].lower()

        try:
            if command == 'info':
                info()
            # Факториал и Фибоначчи
            elif command == 'factorial_iter':
                print(factorial_iter(parse_int(user_input)))
            elif command == 'factorial_rec':
                print(factorial_recursive(parse_int(user_input)))
            elif command == 'fibonacci_iter':
                print(fibo_iter(parse_int(user_input)))
            elif command == 'fibonacci_rec':
                print(fibo_recursive(parse_int(user_input)))
            # Сортировки
            elif command == 'bubble_sort':
                print(bubble_sort(*parse_sort(user_input)))
            elif command == 'quick_sort':
                print(quick_sort(*parse_sort(user_input)))
            elif command == 'counting_sort':
                print(count_sort(*parse_sort(user_input)))
            elif command == 'radix_sort_int':
                print(radix_sort_int(*parse_sort(user_input)))
            elif command == 'radix_sort_str':
                print(radix_sort_str(*parse_sort(user_input)))
            elif command == 'bucket_sort':
                print(bucket_sort(*parse_sort(user_input)))
            elif command == 'heap_sort':
                print(heap_sort(*parse_sort(user_input)))
            # Очереди
            elif command == "create":
                create_queue(user_input)
            elif command == "show":
                show_queue(user_input)
            elif command == "delete":
                delete_queue(user_input)
            elif len(text) >= 2:
                queue_name = text[0]
                command = text[1].lower()
                queue_operation(queue_name, command, user_input)
                
            else:
                print(f"Команда не найдена: '{command}'")
        except Exception as e:
            print(f'ОШИБКА: {e}')

if __name__ == "__main__":
    main()
