import pytest
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.generators import rand_int_array

def test_bubble_sort_benchmark(benchmark):
    """Бенчмарк bubble_sort на случайных данных"""
    arr = rand_int_array(100, -100, 100, seed=42)
    
    result = benchmark(bubble_sort, arr.copy())

    expected = sorted(arr)
    assert result == expected

def test_quick_sort_benchmark(benchmark):
    """Бенчмарк quick_sort на случайных данных"""
    arr = rand_int_array(100, -100, 100, seed=42)
    
    result = benchmark(quick_sort, arr.copy())

    expected = sorted(arr)
    assert result == expected

def test_counting_sort_benchmark(benchmark):
    """Бенчмарк quick_sort на случайных данных"""
    arr = rand_int_array(100, -100, 100, seed=42)
    
    result = benchmark(count_sort, arr.copy())

    expected = sorted(arr)
    assert result == expected

'''def test_bubble_sort_vs_quick_sort(benchmark):
    """Сравнение bubble_sort и quick_sort"""
    arr = rand_int_array(1000, 1, 10000, seed=42)

    def run_bubble():
        return bubble_sort(arr.copy())
    
    def run_quick():
        return quick_sort(arr.copy())

    bubble_result = benchmark.pedantic(run_bubble, rounds=5, iterations=3)
    quick_result = benchmark.pedantic(run_quick, rounds=5, iterations=3)

    expected = sorted(arr)
    assert bubble_result == expected
    assert quick_result == expected'''