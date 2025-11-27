import re
from typing import Dict, Callable, Pattern

LIST_RE: Pattern = re.compile(
    r'''                      
    (?:\"[^\"]*\")
    |(?:\'[^\']*\')
    |(?:[^,\"\'\s]+)
    ''',
    re.VERBOSE,
)

SORT_RE: Pattern = re.compile(
    r'''
    \s*(?P<list>\[.*\])\s*
    (?:key=(?P<key>[^\s]+))?\s*
    (?:cmp=(?P<cmp>[^\s]+))?\s*
    (?:base=(?P<base>[^\s]+))?\s*
    (?:buckets=(?P<buckets>[\d]+))?
    ''',
    re.VERBOSE,
)

KEYS_DICT: Dict[str, Callable] = {
    'abs': lambda x: abs(x),
    'len': lambda x: len(x),
    'case_insensitive': lambda x: x.lower,
    'as_strings': lambda x: str(x),
    
    }

# Функции-компараторы, которые будут доступны пользователю:

def length_then_alpha(x, y):
    if len(x) != len(y):
        return len(x) - len(y)
    else:
        return -1 if x < y else (1 if x > y else 0)
    
def even_first(x, y):
    if x % 2 == y % 2:
        return x - y
    else:
        return -1 if x % 2 == 0 else 1
    
def odd_first(x, y):
    if x % 2 == y % 2:
        return x - y
    else:
        return -1 if x % 2 == 1 else 1

CMPS_DICT: Dict[str, Callable] = {
    'descending': lambda x, y: (y > x) - (y < x),
    'length_then_alpha': length_then_alpha,
    'even_first': even_first,
    'odd_first': odd_first,

}