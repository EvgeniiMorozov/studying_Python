import pytest
from time import time

from lesson_36 import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def measure_time():
    start_time = time()
    yield
    end_time = time() - start_time
    with open('1.txt', 'w', encoding='UTF-8') as f:
        f.write(f'{end_time}')
