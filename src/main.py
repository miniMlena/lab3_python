from src.parsing import parse_sort, parse_int
from src.factorial import factorial_iter, factorial_recursive
from src.fibonacci import fibo_iter, fibo_recursive
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.sortings.radix_int import radix_sort_int
from src.sortings.radix_str import radix_sort_str
from src.sortings.buckets import bucket_sort
from src.sortings.heap import heap_sort

def main() -> None:
    """
    Точка входа в программу
    :return: Данная функция ничего не возвращает
    """
    print('Добро пожаловать в программу для подсчёта факториалов и чисел Фибоначчи, сортировки списков и работы со СТРУКТУРОЙ! Чтобы узнать о всех доступных командах введите info. Для выхода введите quit')
    
    while (user_input:=input("Введите команду: ")).lower() != "quit":
        
        text = user_input.split(maxsplit=1)
        command = text[0].lower()
        
        #try:
        if command == 'info':
            print("This is an example of an interactive loop with Typer.")

        elif command == 'factorial_iter':
            print(factorial_iter(parse_int(user_input)))
        elif command == 'factorial_rec':
            print(factorial_recursive(parse_int(user_input)))
        elif command == 'fibonacci_iter':
            print(fibo_iter(parse_int(user_input)))
        elif command == 'fibonacci_rec':
            print(fibo_recursive(parse_int(user_input)))

            # Сортровки
        elif command == 'bubble_sort':
            print(bubble_sort(*parse_sort(user_input, 'bubble')))
        elif command == 'quick_sort':
            print(quick_sort(*parse_sort(user_input, 'quick')))
        elif command == 'counting_sort':
            print(count_sort(*parse_sort(user_input, 'count')))
        elif command == 'radix_sort_int':
            print(radix_sort_int(*parse_sort(user_input, 'rad_int')))
        elif command == 'radix_sort_str':
            print(radix_sort_str(*parse_sort(user_input, 'rad_str')))
        elif command == 'bucket_sort':
            print(bucket_sort(*parse_sort(user_input, 'bucket')))
        elif command == 'heap_sort':
            print(heap_sort(*parse_sort(user_input, 'heap')))
            
        else:
            print(f"Команда не найдена: '{command}'")
        """except Exception as e:
            print(f'Ошибка: {e}')"""

if __name__ == "__main__":
    main()
