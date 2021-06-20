from typing import Union

from .pizza import PizzaCook
from .pizza import Pizza
from .client import Client


class PizzeriaFacade:
    """
    Фасад пиццерии
    """
    def __init__(self):
        self.cook = PizzaCook()  # В ресторане есть "повар" пиццы, который на самом деле Директор

    def cook_pizza(self, pizza: str) -> Pizza:
        """
        Возвращает готовую пиццу
        """
        return self.cook.make_pizza(pizza)

    def make_order(self, client: Client, pizza: str) -> Union[None, Pizza]:
        """
        Обрабатывает заказ клиента
        """
        pizza = self.cook_pizza(pizza)
        pizza_cost = pizza.get_price()
        client_money = client.get_money()
        if client_money >= pizza_cost:
            return pizza
        else:
            print(f'Не хватает денег! {pizza.name} стоит: {pizza_cost}, а у клиента {client_money}')
