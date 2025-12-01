from typing import Dict
from src.benchmarks.timeit_once import timeit_once
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.sortings.radix_int import radix_sort_int
from src.sortings.buckets import bucket_sort
from src.sortings.heap import heap_sort
from src.generators import *

arrays = {
    "small_random": rand_int_array(100, 1, 1000, seed=42),
    "medium_random": rand_int_array(1000, 1, 10000, seed=42),
    "large_random": rand_int_array(5000, 1, 50000, seed=42),
    "nearly_sorted": nearly_sorted(1000, 50, seed=42),
    "many_duplicates": many_duplicates(1000, k_unique=10, seed=42),
    "reverse_sorted": reverse_sorted(1000),
}

algos = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "count_sort": count_sort,
    "radix_sort": radix_sort_int,
    "bucket_sort": bucket_sort,
    "heap_sort": heap_sort,
    "builtin_sorted": sorted,
}

def benchmark_sorts() -> Dict[str, Dict[str, float]]:
    """
    Запускает бенчмарки для сортировок на разных наборах данных
    :returns: Словарь с результатами {название_алгоритма: {название_массива: время}}
    """
    results = {}
    
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        
        for array_name, array in arrays.items():
            test_array = array.copy()

            time_taken, res = timeit_once(algo_func, test_array)
            results[algo_name][array_name] = time_taken

            expected = sorted(array)
            assert algo_func(array.copy()) == expected

    print("\n" + "="*110)
    print("БЕНЧМАРК: СОРТИРОВКИ")
    print("="*110)

    header = " " * 17
    for array_name in arrays.keys():
        header += f" {array_name:>14}"
    print(header)
    print("-" * 110)

    for algo_name, algo_results in results.items():
        row = f"{algo_name:<15}"
        for array_name in arrays.keys():
            time_taken = algo_results[array_name]
            row += f" {time_taken:>14.6f}"
        print(row)

    return results
