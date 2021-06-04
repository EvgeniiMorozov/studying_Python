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

# Попытка реализации паттерна Строитель (с директором).

from abc import ABC, abstractmethod


# Ингредиенты для приготовления паст.

PASTA = {"spaghetti": "спагетти", "fettuccine": "фетучини", "fusilli": "фузилли"}
SAUCE = {"cream_sauce": "сливочный соус", "egg_sauce": "яичный соус", "tomato_sauce": "томатный соус"}
TOPPING = {
    "bacon": "бекон",
    "carrot": "морковь",
    "celery": "сельдерей",
    "parmesan": "сыр Пармезан",
    "chopped_meat": "мясной фарш",
    "mushrooms": "грибы",
    "spinach": "шпинат",
}
ADDITIVE = {"pepper": "перец", "parsley": "петрушка", "parmesan": "сыр Пармезан"}


class Pasta:
    def __init__(self, name):
        """
        Конструктор класса пасты.

        :param name: название пасты
        :param pasta: тип макарон
        :param sauce: соус
        :param topping: начинка
        :param additive: добавка
        """
        self.name = name
        self.pasta_type = None
        self.sauce = None
        self.topping = None
        self.additive = None

    def __str__(self):
        info: str = (
            f"{self.name} состоит из:\n"
            f"\t- паста: {self.pasta_type};\n"
            f"\t- соус: {self.sauce};\n"
            f"\t- начинка: {self.topping};\n"
            f"\t- по желанию можно добавить {self.additive}."
        )
        return info


class IPastaBuilder(ABC):
    """
    Абстрактный класс, задающий интерфейса строителя.
    """

    @abstractmethod
    def add_pasta(self):
        """Метод, добавляющий пасту (макароны) в приготовляемое блюдо."""
        pass

    @abstractmethod
    def add_sauce(self):
        """Метод, добавляющий соус в приготовляемое блюдо."""
        pass

    @abstractmethod
    def add_topping(self):
        """Метод, добавляющий начинку в приготовляемое блюдо."""
        pass

    @abstractmethod
    def add_additive(self):
        """Метод, добавляющий различные добавки в приготовляемое блюдо."""
        pass

    @abstractmethod
    def get_cooked_pasta(self):
        """Метод, возвращающий приготовленное блюдо (пасту)."""
        pass


class Director:

    """ Класс Director, отвечающий за поэтапное приготовление пасты."""

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: IPastaBuilder):
        self.builder = builder

    def cook_pasta(self):
        if not self.builder:
            raise ValueError('Рецепт (builder) не выбран!')
        self.builder.add_pasta()
        self.builder.add_sauce()
        self.builder.add_topping()
        self.builder.add_additive()


# Реализация конкретных строителей для приготовления паст.


class PastaBologneseBuilder(IPastaBuilder):
    def __init__(self):
        self.pasta = Pasta("Паста Болоньезе")

    def add_pasta(self):
        self.pasta.pasta_type = PASTA['spaghetti']
        
    def add_sauce(self):
        self.pasta.sauce = SAUCE['tomato_sauce']

    def add_topping(self):
        self.pasta.topping = [TOPPING['carrot'], TOPPING['celery'], TOPPING['chopped_meat']]

    def add_additive(self):
        self.pasta.additive = [ADDITIVE['parmesan']]

    def get_cooked_pasta(self):
        return self.pasta


class PastaCarbonaraBuilder(IPastaBuilder):
    def __init__(self):
        self.pasta = Pasta("Паста Карбонара")

    def add_pasta(self):
        self.pasta.pasta_type = PASTA['spaghetti']

    def add_sauce(self):
        self.pasta.sauce = SAUCE['egg_sauce']

    def add_topping(self):
        self.pasta.topping = TOPPING['bacon']

    def add_additive(self):
        self.pasta.additive = [ADDITIVE['parmesan']]

    def get_cooked_pasta(self):
        return self.pasta


class FettuccineAlfredoBuilder(IPastaBuilder):
    def __init__(self):
        self.pasta = Pasta("Фетучини Альфредо")

    def add_pasta(self):
        self.pasta.pasta_type = PASTA['fettuccine']

    def add_sauce(self):
        self.pasta.sauce = SAUCE['cream_sauce']

    def add_topping(self):
        self.pasta.topping = TOPPING['parmesan']

    def add_additive(self):
        self.pasta.additive = ADDITIVE['pepper']

    def get_cooked_pasta(self):
        return self.pasta


class MashroomsSpinachBuilder(IPastaBuilder):
    def __init__(self):
        self.pasta = Pasta("Паста с грибами и шпинатом")

    def add_pasta(self):
        self.pasta.pasta_type = PASTA['fusilli']

    def add_sauce(self):
        self.pasta.sauce = SAUCE['cream_sauce']

    def add_topping(self):
        self.pasta.topping = [TOPPING['mushrooms'], TOPPING['spinach']]

    def add_additive(self):
        self.pasta.additive = [ADDITIVE['pepper'], ADDITIVE['parmesan'], ADDITIVE['parsley']]

    def get_cooked_pasta(self):
        return self.pasta


def main():
    cooks = (PastaBologneseBuilder, PastaCarbonaraBuilder, FettuccineAlfredoBuilder, MashroomsSpinachBuilder)
    director = Director()
    for cook in cooks:
        builder = cook()
        director.set_builder(builder)
        director.cook_pasta()
        pasta = builder.get_cooked_pasta()
        print(pasta)


if __name__ == "__main__":
    main()
