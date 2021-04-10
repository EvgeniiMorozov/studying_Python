# Урок 21 - Тестирование.

# Абстрактные классы
from abc import ABC, abstractmethod
import doctest
import unittest

class Furniture(ABC):
    def __init__(self, material):
        self.material = material

    @abstractmethod
    def set_position(self, position):
        raise NotImplemented

    @abstractmethod
    def use(self):
        pass


class Chair(Furniture):
    def set_position(self, position):
        print(f'Поставили стул под стол')

    def use(self):
        print(f'Сесть на стул')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def factorial(n):
    # """
    # Функция, рассчитывающая факториал.
    #
    # >>> factorial(5)
    # 120
    # >>> factorial(6)
    # 720
    # >>> [factorial(n) for n in range(6)]
    # [1, 1, 2, 6, 24, 120]
    # :param n: int
    # :return: int
    # """
    result = 1
    for i in range(2, n+1):
        result *= i
        return result


# Юнит-тестирование / Модульное
# Интеграционное тестирование


class Calculator:

    def add(self, a, b):
        # """
        # >>> calc = Calculator()
        # >>> calc.add(5, 7)
        # 12
        # """
        return a + b

    def sub(self, a, b):
        # """
        # >>> calc = Calculator()
        # >>> calc.sub(5, 7)
        # -2
        # """
        return a - b

    def mul(self, a, b):
        # """
        # >>> calc = Calculator()
        # >>> calc.mul(5, 7)
        # 35
        # """
        return a * b

    def div(self, a, b):
        # """
        # >>> calc = Calculator()
        # >>> calc.div(5, 7)
        # 0.2
        # """
        return a / b


def main():
    # Абстрактные классы

    # furniture1 = Furniture()
    # furniture1.set_postion('Куда-нибудь')
    #
    # chair1 = Chair('Wood')
    # chair1.set_position('Кухня')
    
    # Тестирование

    # 1 вариант - с помощью print
    # print(add(2, 7), '<------')

    # 2 вариант - с помощью assert
    # assert add(2, 7) == 9

    # 3 вариант - с помощью библиотеки Doctest
    # doctest.testmod()

    # 4 вариант - библиотека Unittest
    unittest.main()


if __name__ == '__main__':
    main()
