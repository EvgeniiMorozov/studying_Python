from abc import ABC, abstractmethod

from .products.product import IProduct
from .products.sauce import DzatzikiSauce
from .products.sauce import GuacamoleSauce
from .products.sauce import KetchupSauce
from .products.sauce import MayonnaiseSauce
from .products.sauce import MustardSauce
from .products.sausage import BavarianSausage
from .products.sausage import SemiSmokedSausage
from .products.sausage import SoySausage
from .products.topping import CabbageTopping
from .products.topping import ChiliTopping
from .products.topping import FreshVegetablesTopping
from .products.topping import JalapenoTopping
from .products.topping import OnionTopping
from .products.topping import PickledCucumberTopping
from .products.topping import SweetChiliTopping
from .products.topping import SweetPeperTopping
from .products.topping import RelishTopping
from .products.topping import TomatoTopping


class Ingredients(ABC):
    """Абстрактное описание фабрики ингредиентов"""

    @abstractmethod
    def create_ingredient(self, ingredient: str) -> IProduct:
        ...


class SauceIngredient(Ingredients):
    """Фабрика соусов"""

    def create_ingredient(self, ingredient: str) -> IProduct:

        if ingredient == 'горчица':
            return MustardSauce()
        elif ingredient == 'майонез':
            return MayonnaiseSauce()
        elif ingredient == 'кетчуп':
            return KetchupSauce()
        elif ingredient == 'гуакамоле':
            return GuacamoleSauce()
        elif ingredient == 'дзадзики':
            return DzatzikiSauce()


class SausageIngredient(Ingredients):
    """Фабрика сосисок"""

    def create_ingredient(self, ingredient: str) -> IProduct:

        if ingredient == 'баварская':
            return BavarianSausage()
        elif ingredient == 'полукопченая':
            return SemiSmokedSausage()
        elif ingredient == 'соевая':
            return SoySausage()


class ToppingIngredient(Ingredients):
    """Фабрика начинок"""

    def create_ingredient(self, ingredient: str) -> IProduct:

        if ingredient == 'капуста':
            return CabbageTopping()
        elif ingredient == 'чили':
            return ChiliTopping()
        elif ingredient == 'свежие овощи':
            return FreshVegetablesTopping()
        elif ingredient == 'халапеньо':
            return JalapenoTopping()
        elif ingredient == 'лук':
            return OnionTopping()
        elif ingredient == 'маринованный огурчик':
            return PickledCucumberTopping()
        elif ingredient == 'сладкий чили':
            return SweetChiliTopping()
        elif ingredient == 'сладкий перец':
            return SweetPeperTopping()
        elif ingredient == 'релиш':
            return RelishTopping()
        elif ingredient == 'помидоры':
            return TomatoTopping()
