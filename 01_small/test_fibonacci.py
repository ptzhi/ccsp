# practice with unit testing
import pytest

from fibonacci import (
    fib_r,
    fib_rc,
    fib_i,
    fib_yield,
    fib_yield_seq,
    fib_mirror_rc,
    fib_mirror_yield,
    fib_mirror_yield_seq,
)

# test input and expected
params_fib = [(5, 5), (0, 0), (1, 1)]


@pytest.mark.parametrize("int, expected", params_fib)
def test_fib_r(int, expected):
    assert fib_r(int) == expected


@pytest.mark.parametrize("int, expected", params_fib)
def test_fib_rc(int, expected):
    assert fib_rc(int) == expected


@pytest.mark.parametrize("int,expected", params_fib)
def test_fib_i(int, expected):
    assert fib_i(int) == expected


params_fib_yield_seq = [(5, [0, 1, 1, 2, 3, 5]), (0, [0]), (1, [0, 1])]


@pytest.mark.parametrize("int, list", params_fib_yield_seq)
def test_fib_yield_seq(int, list):
    assert fib_yield_seq(int) == list


# repeat for mirrored fib
params_fib_mirror = [(-5, -5), (-1, -1), (0, 0), (1, 1), (5, 5)]


@pytest.mark.parametrize("int, expected", params_fib_mirror)
def test_fib_mirror_rc(int, expected):
    assert fib_mirror_rc(int) == expected


params_fib_mirror_yield_seq = [
    (5, [0, 1, 1, 2, 3, 5]),
    (-5, [0, -1, -1, -2, -3, -5]),
    (0, [0]),
    (1, [0, 1]),
    (-1, [0, -1]),
]


@pytest.mark.parametrize("int, list", params_fib_mirror_yield_seq)
def test_fib_mirror_yield_seq(int, list):
    assert fib_mirror_yield_seq(int) == list


# check assert error msg for all functions
def test_fib_assert_error():
    with pytest.raises(AssertionError) as err:
        fib_r(-2)
    assert "fibonacci number must be >= 0" in str(err.value)
    with pytest.raises(AssertionError) as err:
        fib_rc(-2)
    assert "fibonacci number must be >= 0" in str(err.value)
    with pytest.raises(AssertionError) as err:
        fib_i(-2)
    assert "fibonacci number must be >= 0" in str(err.value)
    with pytest.raises(AssertionError) as err:
        fib_yield_seq(-2)
    assert "fibonacci number must be >= 0" in str(err.value)


# check type error for all functions
def test_fib_type_error():
    with pytest.raises(TypeError):
        fib_r("str")
    with pytest.raises(TypeError):
        fib_rc("str")
    with pytest.raises(TypeError):
        fib_i("str")
    with pytest.raises(TypeError):
        fib_yield_seq("str")
