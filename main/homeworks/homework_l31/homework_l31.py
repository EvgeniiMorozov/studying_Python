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


from abc import ABC, abstractmethod
from collections import namedtuple


CARBONARA = {
    'pasta': 'спагетти',
    'sauce': 'яичный соус',
    'topping': 'бекон',
    'additive': 'сыр Пармезан'
}
BOLOGNESE = {
    'pasta': 'спагетти',
    'sauce': 'томатный соус',
    'topping': ('морковь', 'сельдерей', 'мясной фарш'),
    'additive': 'сыр Пармезан'
}
FETTUCCINE_ALFREDO ={
    'pasta': 'фетучини',
    'sauce': 'сливочный соус',
    'topping': 'сыр Пармезан',
    'additive': 'перец'
}
PASTA_MUSHROOMS_AND_SPINACH = {
    'pasta': 'фузилли',
    'sauce': 'сливочный соус',
    'topping': ('грибы', 'шпинат'),
    'additive': ('сыр Пармезан', 'перец', 'петрушка')
}


class IPastaBuilder(ABC):

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
    def __init__(self, name, sauce, topping, additive):
        self.name = name
        self.sauce = sauce
        self.topping = topping
        self.additive = additive

    def __str__(self):
        pass



def main():
    pass


if __name__ == '__main__':
    main()
