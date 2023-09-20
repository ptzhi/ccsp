import pytest

from pi import pi_series

params_leibniz = [
    (0, 0),
    (1, 4),
    (2, 4-(4/3)),
    (3, 4-(4/3)+(4/5)),
]

@pytest.mark.parametrize('test, expected', params_leibniz)
def test_pi_series(test, expected):
    assert pi_series(test) == expected

def test_pi_series_converge():
    assert pi_series(1e5) > 3.141, pi_series(1e5)<3.142
