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


def main():
    pass


if __name__ == '__main__':
    main()
