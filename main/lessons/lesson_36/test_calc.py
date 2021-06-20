import pytest


@pytest.mark.parametrize('a, b, expected_value', [
    (1, 1, 2),
    (-1, 1, 0),
    (1, -1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(a, b, expected_value, calc):
    assert calc.add(a, b) == expected_value


def test_sub(calc):
    assert calc.sub(1, 2) == -1


@pytest.mark.skip
def test_mul(calc):
    assert calc.mul(2, 3) == 6
