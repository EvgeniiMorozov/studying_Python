from core.pizzeria import PizzeriaFacade
from core.client import Client


def main():
    pizzeria = PizzeriaFacade()
    client = Client('Анатолий', 2000)  # Сообщение о нехватке денег и исключение в print'е

    pizza = pizzeria.make_order(client, 'маргарита')
    print(pizza, pizza.get_price())  # Распечатаем состав пиццы и её цену

    pizza = pizzeria.make_order(client, 'салями')
    print(pizza, pizza.get_price())

    pizza = pizzeria.make_order(client, 'индивидуальная')
    print(pizza, pizza.get_price())


if __name__ == '__main__':
    main()
