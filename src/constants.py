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
    \s*(?P<list>\[.*\]
    |rand_int_array\s+[-]?\d+\s+[-]?\d+\s+[-]?\d+
    |nearly_sorted\s+[-]?\d+\s+[-]?\d+
    |many_duplicates\s+[-]?\d+\s+[-]?\d+
    |reverse_sorted\s+[-]?\d+
    |rand_float_array\s+[-]?\d+\s+[-]?\d+(?:\.\d+)?\s+[-]?\d+(?:\.\d+)?
    )?\s*
    (?:key=(?P<key>[^\s]+))?\s*
    (?:cmp=(?P<cmp>[^\s]+))?\s*
    (?:base=(?P<base>[^\s]+))?\s*
    (?:buckets=(?P<buckets>[\d]+))?
    ''',
    re.VERBOSE,
)

LIST_SORT_RE: Pattern = re.compile(
    r'''
    \s*(
    \[[^\[\]]*\]
    |rand_int_array\s+[-]?\d+\s+[-]?\d+\s+[-]?\d+
    |nearly_sorted\s+[-]?\d+\s+[-]?\d+
    |many_duplicates\s+[-]?\d+\s+[-]?\d+
    |reverse_sorted\s+[-]?\d+
    |rand_float_array\s+[-]?\d+\s+[-]?\d+(?:\.\d+)?\s+[-]?\d+(?:\.\d+)?

    |rand_int_array\s+[^keycmpbasebuckets=]*
    |nearly_sorted\s+[^keycmpbasebuckets=]*
    |many_duplicates\s+[^keycmpbasebuckets=]*
    |reverse_sorted\s+[^keycmpbasebuckets=]*
    |rand_float_array\s+[^keycmpbasebuckets=]*
    )
    ''',
    re.VERBOSE,
)

KEY_RE: Pattern =  re.compile(
    r'''
    key=([^\s]+)
    ''',
    re.VERBOSE,
)

CMP_RE: Pattern = re.compile(
    r'''
    cmp=([^\s]+)
    ''',
    re.VERBOSE,
)

BASE_RE: Pattern = re.compile(
    r'''
    base=([^\s]+)
    ''',
    re.VERBOSE,
)

BUCKETS_RE: Pattern = re.compile(
    r'''
    buckets=([\d]+)
    ''',
    re.VERBOSE,
)

KEYS_DICT: Dict[str, Callable] = {
    'abs': lambda x: abs(x),
    'len': lambda x: len(x),
    'case_insensitive': str.lower,
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
