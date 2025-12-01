import pytest
from src.constants import KEYS_DICT, CMPS_DICT
from src.generators import rand_int_array
from src.sortings.bubble import bubble_sort
from src.sortings.quick import quick_sort
from src.sortings.counting import count_sort
from src.sortings.radix_int import radix_sort_int
from src.sortings.radix_str import radix_sort_str
from src.sortings.buckets import bucket_sort
from src.sortings.heap import heap_sort


def test_bubble_sort():
    """Bubble sort с ключами и компараторами"""
    
    arr = [-5, 2, -1, 4, -3]
    result = bubble_sort(arr.copy(), key=KEYS_DICT['abs'])
    expected = sorted(arr, key=abs)
    assert result == expected

    arr = [1, 2, 3, 4, 5]
    result = bubble_sort(arr.copy(), cmp=CMPS_DICT['descending'])
    expected = sorted(arr, reverse=True)
    assert result == expected

    arr = [-5, 2, -1, 4, -3]
    result = bubble_sort(
        arr.copy(), 
        key=KEYS_DICT['abs'], 
        cmp=CMPS_DICT['descending']
    )
    expected = sorted(arr, key=abs, reverse=True)
    assert result == expected

def test_quick_sort():
    """Быстрая сортировка с ключами и компараторами"""

    arr = [-10, 5, -1, 3, -7]
    result = quick_sort(arr.copy(), key=KEYS_DICT['abs'])
    expected = sorted(arr, key=abs)
    assert result == expected

    arr = [4, 7, 2, 9, 1, 6]
    result = quick_sort(arr.copy(), cmp=CMPS_DICT['odd_first'])

    assert result[:3] == [1, 7, 9]
    assert result[3:] == [2, 4, 6]

def test_heap_sort():
    """Сортировка кучей с ключами и компараторами"""

    arr = [101, 11, 2, 20]
    result = heap_sort(arr.copy(), key=KEYS_DICT['as_strings'])
    expected = sorted(arr, key=str)
    assert result == expected

    arr = ["python", "java", "c", "cpp", "javascript"]
    result = heap_sort(arr.copy(), cmp=CMPS_DICT['length_then_alpha'])

    assert result == ["c", "cpp", "java", "python", "javascript"]

    arr = [3, 1, 4, 1, 5]
    result = heap_sort(arr.copy(), cmp=CMPS_DICT['descending'])
    expected = sorted(arr, reverse=True)
    assert result == expected

def test_count_sort():
    """Сортировка счетом с ключами"""

    arr = [-5, 2, -1, 4, -3, 1]
    result = count_sort(arr.copy(), key=KEYS_DICT['abs'])
    expected = sorted(arr, key=abs)
    assert result == expected

def test_radix_sort_int():
    """Поразрядная сортировка для целых чисел с ключами"""

    arr = ["Apple", "banana", "CHERRY", "date"]
    result = radix_sort_int(arr.copy(), key=KEYS_DICT['len'])

    expected = sorted(arr, key=len)
    assert result == expected

def test_radix_sort_str():
    """Поразрядная сортировка для строк с ключами"""

    arr = ["Apple", "banana", "CHERRY", "date"]
    result = radix_sort_str(arr.copy(), key=KEYS_DICT['case_insensitive'])
    expected = sorted(arr, key=str.lower)
    assert result == expected

def test_bucket_sort():
    """Корзинная сортировка с ключами"""

    arr = ["Apple", "banana", "CHERRY", "date"]
    
    result = bucket_sort(arr.copy(), key=KEYS_DICT['len'])
    expected = sorted(arr, key=len)
    assert result == expected

    arr = [-0.3, 0.1, 0.9, -0.5, 0.7]

    result = bucket_sort(arr.copy(), key=KEYS_DICT['abs'])
    expected = sorted(arr, key=abs)
    assert result == expected