# https://docs.python.org/3/library/bisect.html#module-bisect

from bisect import bisect_left, bisect_right

def index(a, x):
    'locate leftmost value exactly equal to x in a'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'fight rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'find leftmost value greater than x'
    i = bisect_right(a, x)
    if i!=len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i!=len(a):
        return a[i]
    raise ValueError
