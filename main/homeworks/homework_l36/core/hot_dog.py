from functools import reduce

from .products.product import IProduct
from .ingredients import SauceIngredient
from .ingredients import SausageIngredient
from .ingredients import ToppingIngredient


class HotDog:
    """Класс хот-дога"""

    def __init__(self, name):
        self.name = name
        self.ingredients = ['булочка']
        self.price = 150

    def add_ingredient(self, ingredient: IProduct) -> None:
        """Добавляем переданный ингредиент в список ингредиентов"""
        self.ingredients.append(ingredient)

    def get_price(self) -> int:
        """Итоговый расчёт цены"""
        total_price = self.price
        for ingredient in self.ingredients[1:]:
            total_price += ingredient.price
        return total_price

    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.ingredients))}"


class IHotDogBuilder:
    """Интерфейс строителя хот-догов"""

    def __init__(self, name):
        self.hot_dog = HotDog(name)
        self.sauce = SauceIngredient()
        self.sausage = SausageIngredient()
        self.topping = ToppingIngredient()

    def add_sauce(self, sauce: str) -> None:
        sauce = self.sauce.create_ingredient(sauce)
        self.hot_dog.add_ingredient(sauce)

    def add_sausage(self, sausage: str) -> None:
        sausage = self.sausage.create_ingredient(sausage)
        self.hot_dog.add_ingredient(sausage)

    def add_topping(self, topping: str) -> None:
        topping = self.topping.create_ingredient(topping)
        self.hot_dog.add_ingredient(topping)

    def make_hot_dog(self) -> HotDog:
        pass


class AmericanBuilder(IHotDogBuilder):
    """Строитель классического американского хот-дога"""

    def __init__(self, name='Американский хот-дог'):
        super().__init__(name)

    def make_hot_dog(self, sauce='кетчуп', sausage='баварская', topping='маринованный огурчик') -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class GuacamoleBuilder(IHotDogBuilder):
    """Строитель хот-дога с гуакамоле"""

    def __init__(self, name='Хот-дог с гуакомоле'):
        super().__init__(name)

    def make_hot_dog(self, sauce='гуакамоле', sausage='полукопченая', topping='помидоры') -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class SweetChiliBuilder(IHotDogBuilder):
    """Строитель хот-дога со сладким чили"""

    def __init__(self, name='Хот-дог со сладким чили'):
        super().__init__(name)

    def make_hot_dog(self, sauce='', sausage='полукопченая', topping='сладкий чили') -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class RelishBuilder(IHotDogBuilder):
    """Строитель хот-дога с релишем"""

    def __init__(self, name='Хот-дог с релишем'):
        super().__init__(name)

    def make_hot_dog(self, sauce='горчица', sausage='баварская', topping='релиш') -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class DzatzikiBuilder(IHotDogBuilder):
    """Строитель хот-дога с дзадзики"""

    def __init__(self, name='Хот-дог с дзадзики'):
        super().__init__(name)

    def make_hot_dog(self, sauce='дзадзики', sausage='соевая', topping='свежие овощи') -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class IndividualBuilder(IHotDogBuilder):
    """Строитель хот-дога по индивидуальному заказу"""

    def __init__(self, name='Индивиуальный заказ'):
        super().__init__(name)

    def make_hot_dog(self, sauce=None, sausage=None, topping=None) -> HotDog:
        self.add_sauce(sauce)
        self.add_sausage(sausage)
        self.add_topping(topping)
        return self.hot_dog


class HotDogCook:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder: IHotDogBuilder) -> None:
        self.builder = builder

    def cook_hot_dog(self, order: str) -> HotDog:
        if order == 'американский':
            self.set_builder(AmericanBuilder())
            return self.builder.make_hot_dog()

        elif order == 'хот-дог с гуакамоле':
            self.set_builder(GuacamoleBuilder())
            return self.builder.make_hot_dog()

        elif order == 'хот-дог со сладким чили':
            self.set_builder(SweetChiliBuilder())
            return self.builder.make_hot_dog()

        elif order == 'хот-дог с релишем':
            self.set_builder(RelishBuilder())
            return self.builder.make_hot_dog()

        elif order == 'хот-дог с дзадзики':
            self.set_builder(DzatzikiBuilder())
            return self.builder.make_hot_dog()

        elif order == 'индивидуальный':
            self.set_builder(IndividualBuilder())
            print('У нас в наличии соусы: горчица, кетчуп, майонез, гуакамоле, дзадзики')
            sauce = input('Выберите соус: ')
            print('У нас в наличии сосиски: баварская, полукопченая, соевая')
            sausage = input('Выберите сосиску: ')
            print('У нас в наличии начинки: капуста, чили, свежие овощи, халапеньо, лук, маринованный огурчик, сладкий чили, релиш, помидоры')
            topping = input('Выберите начинку: ')
            return self.builder.make_hot_dog(sauce, sausage, topping)
