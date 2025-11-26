import typer
from src.app_errors import AppError
from src.parsing import parse_sort
from src.sortings.bubble import bubble_sort

app = typer.Typer()

@app.command()
def interactive_session():
    """Запускает интерактивную сессию"""

    typer.echo('''Добро пожаловать в программу для подсчёта факториалов и чисел Фибоначчи, сортировки списков и работы со СТРУКТУРОЙ! Чтобы узнать о всех доступных командах введите info. Для выхода введите quit''')
    
    while (user_input:=typer.prompt("Введите команду")).lower() != "quit":
        
        text = user_input.split(maxsplit=1)
        command = text[0].lower()
        
        try:
            if command == 'hello':
                typer.echo("Hello there!")
            elif command == 'info':
                typer.echo("This is an example of an interactive loop with Typer.")
            elif command == 'bubble_sort':
                print(bubble_sort(*parse_sort(user_input)))
            else:
                typer.echo(f"Команда не найдена: '{command}'")
        except Exception as e:
            print(f'Ошибка: {e}')

if __name__ == "__main__":
    app()
