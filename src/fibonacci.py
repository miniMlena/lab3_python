from math import sqrt
import functools

def fibo(n: int) -> int:
    return int(1 / sqrt(5) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n))
# сделать показатель в 2 раза меньше, основание в квадрат, будет логарифмическая сложность

def fibo_alt(n: int) -> int: #максимум 20577
    f1, f2 = 0, 1
    for _ in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2

@functools.cache
def fibo_recursive(n: int) -> int: #максимум 1996
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 2) + fibo_recursive(n - 1)
    
print(fibo_alt())