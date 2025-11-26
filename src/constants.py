import re

LIST_RE = re.compile(
    r'''                      
    (?:\"[^\"]*\")
    |(?:\'[^\']*\')
    |(?:[^,\"\'\s]+)
    ''',
    re.VERBOSE,
)

SORT_RE = re.compile(
    r'''
    \s*(?P<list>\[.*\])\s*
    (?:key=(?P<key>[^\s]+))?\s*
    (?:cmp=(?P<cmp>[^\s]+))?\s*
    (?:base=(?P<base>[^\s]+))?\s*
    (?:buckets=(?P<buckets>[\d]+))?
    ''',
    re.VERBOSE,
)

'''com = '[1, 2, \'a,bc\']    key=BEST_KEY1'
print(SORT_RE.findall(com))
mat = SORT_RE.match(com)
print(mat.group('list'))
print(mat.group('key'))
print(mat.group('cmp'))'''

"""text = 'ф1, 2, 3, "ab c"'
print(re.findall(LIST_RE, text))"""

keys_dict = {
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

cmps_dict = {
    'descending': lambda x, y: (y > x) - (y < x),
    'length_then_alpha': length_then_alpha,
    'even_first': even_first,
    'odd_first': odd_first,

}