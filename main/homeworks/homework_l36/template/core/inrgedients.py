"""
Здесь находятся фабрики ингредиентов.
"""

from abc import ABC, abstractmethod

from .products.product import IProduct
from .products.sauce import AlfredoSauce
from .products.sauce import TomatoSauce
from .products.sauce import MayoSauce
from .products.meat import BeefMeat
from .products.meat import PorkMeat
from .products.meat import SalamiMeat
from .products.topping import MushroomTopping
from .products.topping import CucumberTopping
from .products.topping import ChiliTopping
from .products.topping import CheeseTopping


class Ingredients(ABC):
    """
    Абстрактное описание фабрики ингредиентов
    """
    @abstractmethod
    def create_ingredient(self, ingredient: str) -> IProduct:
        ...


class SauceIngredient(Ingredients):
    """
    Фабрика соусов
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'альфредо':
            return AlfredoSauce()
        elif ingredient == 'томатный':
            return TomatoSauce()
        elif ingredient == 'майонезный':
            return MayoSauce()


class MeatIngredient(Ingredients):
    """
    Фабрика мяса
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'баранина':
            return BeefMeat()
        elif ingredient == 'свинина':
            return PorkMeat()
        elif ingredient == 'салями':
            return SalamiMeat()


class ToppingIngredient(Ingredients):
    """
    Фабрика топпингов
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'грибы':
            return MushroomTopping()
        elif ingredient == 'огурцы':
            return CucumberTopping()
        elif ingredient == 'чили':
            return ChiliTopping()
        elif ingredient == 'сыр':
            return CheeseTopping()
