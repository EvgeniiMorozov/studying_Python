import pytest

from lesson_36 import add_func
from lesson_36 import mul_func
from lesson_36 import div_func
from lesson_36 import sub_func


@pytest.mark.calc
def test_sub_func():
    assert sub_func(1, 1) == 0


def test_mul_func():
    assert mul_func(2, 3) == 6


def test_div_func():
    assert div_func(100, 10) == 10
