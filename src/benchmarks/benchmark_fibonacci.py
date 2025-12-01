from src.benchmarks.timeit_once import timeit_once
from src.fibo_fact.fibonacci import fibo_iter, fibo_recursive

def benchmark_fibonacci() -> None:
    """
    Бенчмарк для функций Фибоначчи
    :return: Эта функция ничего не возвращает
    """
    print("\n" + "=" * 45)
    print("БЕНЧМАРК: ЧИСЛА ФИБОНАЧЧИ")
    print("=" * 45)
    
    test_numbers = [5, 10, 20, 30, 100, 500, 1000, 1500]
    
    print(f"{'n':>6} {'fibo_iter':>14} {'fibo_recursive':>20}")
    print("-" * 45)
    
    for n in test_numbers:
        row = f"{n:>6}"

        time_iter, result_iter = timeit_once(fibo_iter, n)
        row += f" {time_iter:>13.6f}"

        time_rec, result_rec = timeit_once(fibo_recursive, n)
        row += f" {time_rec:>17.6f}"

        if result_iter is not None and result_rec is not None:
            assert result_iter == result_rec
        
        print(row)