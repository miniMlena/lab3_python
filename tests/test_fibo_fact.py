import pytest
from math import factorial
from src.fibo_fact.factorial import factorial_iter, factorial_recursive
from src.fibo_fact.fibonacci import fibo_iter, fibo_recursive
from src.app_errors import AppError

def test_factorial_iter_correct():
    
    tests = [0, 1, 5, 10, 20]
    for n in tests:
        assert factorial_iter(n) == factorial(n)

def test_factorial_recursive_correct():
    tests = [0, 1, 5, 10, 20]
    for n in tests:
        assert factorial_recursive(n) == factorial(n)

def test_fibo_iter_correct():
    
    known = {1: 1, 5: 5, 10: 55, 20: 6765}
    for n, val in known.items():
        assert fibo_iter(n) == val

def test_fibo_recursive_correct():
    known = {1: 1, 5: 5, 10: 55, 20: 6765}
    for n, val in known.items():
        assert fibo_recursive(n) == val

def test_upper_limit_raises():
    with pytest.raises(AppError):
        factorial_iter(1551)
    with pytest.raises(AppError):
        factorial_recursive(1501)
    with pytest.raises(AppError):
        fibo_iter(20501)
    with pytest.raises(AppError):
        fibo_recursive(1901)

def benchmark_func(benchmark, func, n):
    result = benchmark(func, n)
    assert result is not None and isinstance(result, int)
    return result

def test_factorial_iter_benchmark(benchmark):
    benchmark_func(benchmark, factorial_iter, 500)

def test_factorial_recursive_benchmark(benchmark):
    benchmark_func(benchmark, factorial_recursive, 300)

def test_fibo_iter_benchmark(benchmark):
    benchmark_func(benchmark, fibo_iter, 10000)

def test_fibo_recursive_benchmark(benchmark):
    benchmark_func(benchmark, fibo_recursive, 1000)
