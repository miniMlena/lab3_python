import pytest
from src.generators import rand_int_array
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.sortings.radix_int import radix_sort_int
from src.sortings.buckets import bucket_sort
from src.sortings.heap import heap_sort

@pytest.mark.benchmark(group="sorting")
def benchmark_sort(benchmark, sort_func, base_arr):
    def run():
        arr = base_arr.copy()
        return sort_func(arr)
    result = benchmark(run)
    assert result == sorted(base_arr)
    return result

def test_bubble_sort_benchmark(benchmark):
    """Проверкапузырьковой сортировки на случайных данных"""
    arr = rand_int_array(1000, -100, 100, seed=42)
    benchmark_sort(benchmark, bubble_sort, arr.copy())


def test_quick_sort_benchmark(benchmark):
    """Проверка быстрой сортировки на случайных данных"""
    arr = rand_int_array(1000, -100, 100, seed=42)
    benchmark_sort(benchmark, quick_sort, arr.copy())


def test_counting_sort_benchmark(benchmark):
    """Проверка сортировки счётом на случайных данных"""
    arr = rand_int_array(1000, -100, 100, seed=42)
    benchmark_sort(benchmark, count_sort, arr.copy())


def test_radix_int_sort_benchmark(benchmark):
    """Проверка поразрядной сортировки на случайных данных"""
    arr = rand_int_array(1000, 0, 1000, seed=42)
    benchmark_sort(benchmark, radix_sort_int, arr.copy())


def test_bucket_sort_benchmark(benchmark):
    """Проверка корзинной/карманной сортировки на случайных данных"""
    arr = rand_int_array(1000, 0, 1000, seed=42)
    benchmark_sort(benchmark, bucket_sort, arr.copy())


def test_heap_sort_benchmark(benchmark):
    """Проверка сортировки кучей на случайных данных"""
    arr = rand_int_array(1000, -100, 100, seed=42)
    benchmark_sort(benchmark, heap_sort, arr.copy())
