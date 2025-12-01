from src.benchmarks.timeit_once import timeit_once
from src.fibo_fact.factorial import factorial_iter, factorial_recursive

def benchmark_factorial() -> None:
    """
    Бенчмарк для функций факториала
    :return: Эта функция ничего не возвращает
    """
    print("\n" + "=" * 45)
    print("БЕНЧМАРК: ФАКТОРИАЛЫ")
    print("=" * 45)

    test_numbers = [5, 10, 20, 50, 100, 200, 500, 1000, 1500]
    
    print(f"{'n':>6} {'fact_iter':>14} {'fact_recursive':>18}")
    print("-" * 45)
    
    for n in test_numbers:
        row = f"{n:>6}"

        time_iter, result_iter = timeit_once(factorial_iter, n)
        row += f" {time_iter:>13.6f}"

        time_rec, result_rec = timeit_once(factorial_recursive, n)
        row += f" {time_rec:>16.6f}"

        if result_iter is not None and result_rec is not None:
            assert result_iter == result_rec
        
        print(row)