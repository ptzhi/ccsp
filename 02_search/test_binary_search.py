import pytest

from binary_search import binary_search_r, binary_search_i

params_true = [
        # odd
        (1, [1,2,3]),
        (2, [1,2,3]),
        (3, [1,2,3]),
        # even
        (1, [1,2,3,4]),
        (2, [1,2,3,4]),
        (3, [1,2,3,4]),
        (4, [1,2,3,4]),
        ]
@pytest.mark.parametrize('key, struct', params_true)
def test_binary_search_r_true(key, struct):
    assert binary_search_r(key, struct) == True

@pytest.mark.parametrize('key, struct', params_true)
def test_binary_search_i_true(key, struct):
    assert binary_search_i(key, struct) == True


params_false = [
        # odd
        (0, [1,2,3]),
        (4, [1,2,3]),
        (-4, [1,2,3]),
        #even
        (0, [1,2,3,4]),
        (5, [1,2,3,4])
        ]
@pytest.mark.parametrize('key, struct', params_false)
def test_binary_search_r_false(key, struct):
    assert binary_search_r(key, struct) == False

@pytest.mark.parametrize('key, struct', params_false)
def test_binary_search_i_false(key, struct):
    assert binary_search_i(key, struct) == False


params_edge = [
        # odd
        (0, []),
        (-1, []),
        ]
@pytest.mark.parametrize('key, struct', params_edge)
def test_binary_search_r_error(key, struct):
    with pytest.raises(IndexError):
        binary_search_r(key, struct)

@pytest.mark.parametrize('key, struct', params_edge)
def test_binary_search_i_edge(key, struct):
    assert binary_search_i(key, struct) == False

