from functools import cache, wraps

""" variations of getting nth fibonacci number from sequence 0 1 1 2 3 5... starting with 0th"""


# set up count calls wrapper
def count_calls(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return f(*args, **kwargs)

    wrapper.count = 0
    return wrapper


# recursive, no cache
@count_calls
def fib_r(n: int) -> int:
    assert n >= 0, "fibonacci number must be >= 0"
    if n < 2:
        return n
    return fib_r(n - 1) + fib_r(n - 2)


# recursive, caching
@count_calls
@cache
def fib_rc(n: int) -> int:
    assert n >= 0, "fibonacci number must be >= 0"
    if n < 2:
        return n
    return fib_rc(n - 1) + fib_rc(n - 2)


# iterative
def fib_i(n: int) -> int:
    assert n >= 0, "fibonacci number must be >= 0"
    if n < 2:
        return n
    first, second = 0, 1
    for i in range(2, n + 1):
        num = first + second
        first = second
        second = num
    return num


# yield fib
def fib_yield(n: int):
    yield 0
    if n >= 1:
        yield 1
    first, second = 0, 1
    for i in range(2, n + 1):
        num = first + second
        first = second
        second = num
        yield num


def fib_yield_seq(n):
    assert n >= 0, "fibonacci number must be >= 0"
    return [x for x in fib_yield(n)]


# for mirrored fibonacci ... -5 -3 -2 -1 -1 0 1 1 2 3 4 5...
@count_calls
@cache
def fib_mirror_rc(n: int) -> int:
    if -2 < n < 2:
        return n
    elif n < -1:
        return fib_mirror_rc(n + 1) + fib_mirror_rc(n + 2)
    else:
        return fib_mirror_rc(n - 1) + fib_mirror_rc(n - 2)


# yield fib
def fib_mirror_yield(n: int):
    yield 0
    first, second = 0, 1
    if n >= 1:
        yield 1
        for i in range(2, n + 1):
            num = first + second
            first = second
            second = num
            yield num
    elif n <= -1:
        yield -1
        second = -second
        i = -1
        while i > n:
            i -= 1
            num = first + second
            first = second
            second = num
            yield num


def fib_mirror_yield_seq(n):
    return [x for x in fib_mirror_yield(n)]
