from typing import Union

from .hot_dog import HotDogCook
from .hot_dog import HotDog
from .client import Client


class KioskFacade:
    """Фасад киоска по продаже хот-догов"""

    def __init__(self):
        self.cook = HotDogCook()

    def cook_hot_dog(self, hot_dog: str) -> HotDog:
        return self.cook.cook_hot_dog(hot_dog)

    def make_order(self, client: Client, hot_dog: str) -> Union[None, HotDog]:
        hot_dog = self.cook_hot_dog(hot_dog)
        hot_dog_cost = hot_dog.get_price()
        client_money = client.get_money()
        if client_money >= hot_dog_cost:
            return hot_dog
        else:
            print(f'Не хватает денег! {hot_dog.name} стоит: {hot_dog_cost}, а у клиента {client_money}')
