from abc import ABC, abstractmethod

from .products.product import IProduct
from .products.sause import DzatzikiSause
from .products.sause import GuacamoleSause
from .products.sause import KetchupSause
from .products.sause import MayonnaiseSause
from .products.sause import MustardSause
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


class SauseIngredient(Ingredients):
    """Фабрика соусов"""

    def create_ingredient(self, ingredient: str) -> IProduct:

        if ingredient == 'горчица':
            return MustardSause()
        elif ingredient == 'майонез':
            return MayonnaiseSause()
        elif ingredient == 'кетчуп':
            return KetchupSause()
        elif ingredient == 'гуакомоле':
            return GuacamoleSause()
        elif ingredient == 'дзадзики':
            return DzatzikiSause()


class SausageIngredient(Ingredients):
    """Фабрика сосисок"""

    def create_ingredient(self, ingredient: str) -> IProduct:

        if ingredient == 'баварская':
            return BavarianSausage()
        elif ingredient == 'полукопченная':
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
