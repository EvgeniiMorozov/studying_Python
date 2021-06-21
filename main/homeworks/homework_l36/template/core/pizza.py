"""
Здесь находятся строители пицц
"""

from functools import reduce

from .products.product import IProduct
from .inrgedients import SauceIngredient
from .inrgedients import MeatIngredient
from .inrgedients import ToppingIngredient


class Pizza:
    """
    Описание пиццы
    """
    def __init__(self, name):
        self.name = name
        self.ingredients = ['тесто']  # Обыкновенный список
        self.price = 200  # Стартовая цена пиццы

    def add_ingredient(self, ingredient: IProduct) -> None:
        """
        Добавляет переданный ингредиент в список ингредиентов
        """
        self.ingredients.append(ingredient)

    def get_price(self) -> int:
        """
        Возвращает итоговую стоимость пиццы, исходя из стартовой
        цены, а также стоимости её ингредиентов.
        """
        total_price = self.price
        for ingredient in self.ingredients[1:]:
            total_price += ingredient.price
        return total_price

    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.ingredients))}"


class PizzaBuilder:
    """
    Строитель пиццы. На его основе создаются конкретные строители пицц.
    """
    def __init__(self, name):
        self.pizza = Pizza(name)  # Пустая пицца
        self.sauce = SauceIngredient()  # Фабрика соусов
        self.meat = MeatIngredient()  # Фабрика мяса
        self.topping = ToppingIngredient()  # Фабрика топпингов

    def add_sauce(self, sauce: str) -> None:
        """
        Добавляет соус
        """
        sauce = self.sauce.create_ingredient(sauce)
        self.pizza.add_ingredient(sauce)

    def add_meat(self, meat: str) -> None:
        """
        Добавляет мясо
        """
        meat = self.meat.create_ingredient(meat)
        self.pizza.add_ingredient(meat)

    def add_topping(self, topping: str) -> None:
        """
        Добавляет топпинг
        """
        topping = self.topping.create_ingredient(topping)
        self.pizza.add_ingredient(topping)

    def make_pizza(self, sauce=None, meat=None, topping=None) -> Pizza:
        """
        Метод, собирающий пиццу в правильной последовательности
        """
        pass


class MargaritaBuilder(PizzaBuilder):
    """
    Строитель пиццы Маргариты
    """
    def __init__(self, name='Маргарита'):
        super().__init__(name)

    def make_pizza(self, sauce='томатный', meat=None, topping='сыр') -> Pizza:
        self.add_sauce(sauce)
        self.add_topping(topping)
        return self.pizza


class SalamiBuilder(PizzaBuilder):
    """
    Строитель пиццы Салями
    """
    def __init__(self, name='Салями'):
        super().__init__(name)

    def make_pizza(self, sauce='томатный', meat='салями', topping='грибы') -> Pizza:
        self.add_sauce(sauce)
        self.add_meat(meat)
        self.add_topping(topping)
        return self.pizza


class IndividualBuilder(PizzaBuilder):
    """
    Строитель индивидуальной пиццы
    """
    def __init__(self, name='Индивидуальная пицца'):
        super().__init__(name)

    def make_pizza(self, sauce=None, meat=None, topping=None) -> Pizza:
        self.add_sauce(sauce)
        self.add_meat(meat)
        self.add_topping(topping)
        return self.pizza


class PizzaCook:
    """
    Директор, который управляет строителями пицц
    """
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: PizzaBuilder) -> None:
        self.builder = builder

    def make_pizza(self, pizza: str) -> Pizza:
        if pizza == 'маргарита':
            self.set_builder(MargaritaBuilder())
            return self.builder.make_pizza()
        elif pizza == 'салями':
            self.set_builder(SalamiBuilder())
            return self.builder.make_pizza()
        elif pizza == 'индивидуальная':
            self.set_builder(IndividualBuilder())
            sauce = input('Какой соус: ')
            meat = input('Какое мясо: ')
            topping = input('Какой топпинг: ')
            return self.builder.make_pizza(sauce, meat, topping)
