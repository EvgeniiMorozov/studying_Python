import pytest


@pytest.mark.parametrize('a, b, expected_value', [
    (1, 1, 2),
    (-1, 1, 0),
    (1, -1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add(a, b, expected_value, calc, measure_time):
    assert calc.add(a, b) == expected_value
