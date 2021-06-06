# Паттерны проектирования. Структурные паттерны.
# Модуль enum.
from enum import Enum, auto


class Variables(Enum):
    one = 1
    two = 2
    three = 3
    data = {1: 'one', 2: 'two', 3: 'three'}


# Паттерны проектирования. Структурные паттерны.

# Adapter, Адаптер, Wrapper*, Обёртка*.

class Strs:  # класс со "старым" функционалом.
    def get_some_data(self):
        return '12345'


class Nums:  # класс с "новым" функционалом.
    def get_some_data(self):
        return 6789


class NumsToStrAdapter(Nums):
    def get_some_data(self):
        return str(super().get_some_data())


# Фасад, Facade, Факад.


# class VideoConverter:
#     pass
#
#
# class AudioConverter:
#     pass
#
#
# class ImageConverter:
#     pass
#
#
# class Database:
#     pass

class Kitchen:
    def prepare_food(self):
        print('Еда готовится')

    def give_food(self):
        print('Еда готова, забирайте!')


class Waiter:
    def take_order(self, client):
        print(f'Официант принял заказ клиента {client.get_name()}')

    def send_order_to_kitchen(self, kitchen):
        print('Официант передал заказ на кухню')

    def serve_order_to_client(self, client):
        print(f'Блюда готовы и переданы клиенту {client.get_name()}')


class Client:
    def __init__(self, name):
        self.__name = name

    def request_menu(self, menu):
        print(f'Клиент {self.__name} ознакамливается с меню {menu}')

    def make_order(self):
        print(f'Клиент {self.__name} делает заказ')

    def eat_food(self):
        print(f'Клиент {self.__name} ест еду')

    def get_name(self):
        return self.__name


class RestaurantFacade:
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()
        self.menu = {
            'веган': 'вегетарианское меню',
            'мясоед': 'меню с мясом',
            'всеяд': 'мясо и зелень'
        }

    def get_menu(self, type):
        return self.menu[type]

    def take_order(self, client):
        self.waiter.take_order(client)
        self.waiter.send_order_to_kitchen(self.kitchen)
        self.kitchen_work()
        self.waiter.serve_order_to_client(client)

    def kitchen_work(self):
        self.kitchen.prepare_food()
        self.kitchen.give_food()


# Bridge, Мост.
class IDevice:
    def __init__(self):
        self.enabled = False
        self.volume = 10

    def get_volume(self):
        return self.volume

    def set_volume(self):
        pass


class TV(IDevice):
    def set_volume(self):
        self.volume = self.get_volume() + 1

    def turn_off(self):
        print('Выключаем ...')


class Radio(IDevice):
    def set_volume(self):
        self.volume = self.get_volume() + 5

    def turn_off(self):
        print('Выключаем ...')


class Remote:
    def __init__(self, device):
        self.device = device

    def set_volume(self):
        pass

    def turn_off(self):
        pass


class Remoter(Remote):
    def set_volume(self):
        print("Нажимаем на кнопку пульта")
        self.device.set_volume()

    def turn_off(self):
        print("Нажимаем на кнопку выключения на пульте")
        self.device.turn_off()


class Buttons(Remote):
    def set_volume(self):
        print(f'Подошли к {self.device} и нажали на кнопку')
        self.device.set_volume()

    def turn_off(self):
        print(f"Подошли к {self.device} и нажали на кнопку выключения")
        self.device.turn_off()


def main():

    # Модуль enum.

    # print(Variables.one)
    # print(Variables.one.value)
    # print(Variables.one.name)
    # print(type(Variables.data))
    # print(Variables.data.value)

    # Adapter, Адаптер.
    # obj = Strs()
    # # obj = Nums()
    # obj = NumsToStrAdapter()
    # print('Полученные данные: ' + obj.get_some_data())

    # Фасад.

    restaurant = RestaurantFacade()
    client1 = Client('Vasya')
    client2 = Client('Andrew')

    client1.request_menu('веган')
    restaurant.take_order(client1)

    client2.request_menu('мясоед')
    restaurant.take_order(client2)

    client1.eat_food()
    client2.eat_food()

    # Bridge.

    tv = TV()
    remoter = Remoter(tv)
    buttons_on_body = Buttons(tv)

    remoter.set_volume()
    buttons_on_body.turn_off()


if __name__ == '__main__':
    main()
