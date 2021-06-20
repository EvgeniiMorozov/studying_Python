import pytest

from lesson_36 import add_func


@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, 3),
    (-1, -1, -2),
    (2, 3, 5),
    (-1, 2, 1),
    (2, -3, -1),
    (0, 1, 2)
])
@pytest.mark.calc
def test_add_func(a, b, expected_result):
    assert add_func(a, b) == expected_result


@pytest.mark.calc
def test_add_negative():
    assert add_func(1, -2) == -1


def test_add_negative2():
    assert add_func(-3, -5) == -8