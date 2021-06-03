"""
Создайте приложение для приготовления пасты. Приложение должно уметь
создавать минимум три вида пасты. Классы различной пасты должны иметь
следующие методы:

- Тип пасты;
- Соус;
- Начинка;
- Добавки.

Для реализации используйте любой из пройденных порождающих паттернов.
Для упрощения проверки, в комментарии к коду  напишите название выбранного
паттерна.
"""


import enum
from abc import ABC, abstractmethod
from collections import namedtuple


CARBONARA = ('Паста Карбонара', 'спагетти', 'яичный соус', 'бекон', 'сыр Пармезан')
BOLOGNESE = ('Паста Болоньезе', 'спагетти', 'томатный соус', 'морковь, сельдерей, мясной фарш', 'сыр Пармезан')
FETTUCCINE_ALFREDO = ('Фетучини Альфредо', 'фетучини', 'сливочный соус', 'сыр Пармезан', 'перец')
MUSHROOMS_AND_SPINACH = (
    'Паста с грибами и шпинатом',
    'фузилли',
    'сливочный соус',
    'грибы, шпинат',
    'сыр Пармезан, перец, петрушка'
)


class IPastaBuilder(ABC):
    """
    Абстрактный класс, задающий интерфейса строителя.
    """

    @abstractmethod
    def add_pasta(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def add_additive(self):
        pass


class Pasta:
    def __init__(self, name, pasta, sauce, topping, additive):
        """
        Конструктор класса пасты.

        :param name: название пасты
        :param pasta: тип макарон
        :param sauce: соус
        :param topping: начинка
        :param additive: добавка
        """
        self.name = name
        self.type = pasta
        self.sauce = sauce
        self.topping = topping
        self.additive = additive

    def __str__(self):
        pass


class PastaBologneseBuilder(IPastaBuilder):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
