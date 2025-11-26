from typing import TypeVar, Callable, Any
from src.app_errors import AppError
from src.sortings.quick import quick_sort

T = TypeVar('T')

def bucket_sort(arr: list[T], key: Callable[[T], Any] | None = None,
                buckets: int | None = None) -> list[T]:
    if not arr:
        return arr

    if key is not None:
        values = []
        for a in arr:
            try:
                values.append(key(a))
            except Exception:
                raise AppError(f"Нельзя применить указанный ключ к элементу: {"'" + a + "'" if type(a) is str else a}")
    else:
        values = arr

    for v in values:
        if not (isinstance(v, (int, float)) and v >= 0):
            raise AppError(f"Сортировка bucket_sort работает только с целыми и дробными неотрицательными числами, вы ввели: {"'" + v + "'" if type(v) is str else v}")

    if len(set(values)) == 1:
        return arr
    
    min_val, max_val = min(values), max(values)

    if buckets is None:
        buckets = len(arr)
    buckets_list = [[] for _ in range(buckets)]

    for i in range(len(arr)):
        # Нормализуем значение от 0 до 1
        normalized = (values[i] - min_val) / (max_val - min_val)
        bucket_index = int(normalized * (buckets - 1))
        bucket_index = max(0, min(bucket_index, buckets - 1))
        buckets_list[bucket_index].append(arr[i])
    
    result = []
    for bucket in buckets_list:
        if bucket:
            sorted_bucket = quick_sort(bucket, key=key)
            result.extend(sorted_bucket)
    
    return result