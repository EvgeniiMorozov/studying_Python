"""
Домашнее задание:

1. (Необязательно) Послушать "Научно-технический реп - Полиморфизм"

2. (Обязательно) Реализовать классы и потомки по следующей схеме:

Класс Vehicle (средство передвижения).
У объектов класса Vehicle есть поля:
working_engine - с момента создания равно False, является обозначением того, заведен двигатель или нет

У объектов класса Vehicle есть методы:
start - выводит надпись "Двигатель заведен", если working_engine False и меняет его на True
move - выводит надпись "Средство передвижения едет", если working_engine True
stop - вывод надпись "Двигатель остановлен", если working_engine True и меняет его на False

У класса Vehicle есть потомки:
Tank - танк
Car - машина
Boat - надувная лодка

У объектов класса Tank есть поля:
count_ammo - с момента создания равно 10, боезапас танка

У объектов класса Tank есть методы:
move - выводит надпись "Гусиницы заскрипели от движения", если working_engine True, иначе выдаёт надпись "Нужно завести двигатель"
shoot - выводит надпись "Танк выстрелил" и уменьшает count_ammo на 1, если count_ammo > 0, иначе выдаёт надпись "Снаряды кончились"

У объектов класса Car есть поля:
fuel - с момента создания равно 100, топливо машины

У объектов класса Car есть методы:
start - выводит надпись "Двигатель машины заведён", если working_engine False, и меняет его на True. Если fuel <= 0, выдаёт надпись "Бензина нет"
move - выводит надпись "Машина поехала" и уменьшает fuel на 10, если working_engine True, иначе выдаёт надпись "Машина не заведена",
если fuel во время езды станет <= 0, тогда вывести надпись "Машина заглохла" и установить working_engine на False

У объектов класса Boat есть поля:
air_pressure - с момента создания равно 100, давление воздуха внутри лодки

У объектов класса Boat есть методы:
start - выводит надпись "Мотор лодки гудит", если working_engine False, и меняет его на True. Если если air_pressure <= 0, выдаёт надпись "Лодка тонет!" и двигатель не заводится
move - выводит надпись "Лодка плывёт", если working_engine True, и уменьшает air_pressure на 10, иначе выдаёт надпись "Мотор лодки не заведен"

Все объекты классов никаких дополнительных параметров на вход не получают, то есть их классы вызываются с пустыми скобками.
У классов-потомков только один родитель - Vehicle.
"""


class Vehicle:

    def __init__(self):
        self.working_engine = False

    def start(self):
        if not self.working_engine:
            self.working_engine = True
            print('Двигатель заведён.')

    def move(self):
        if self.working_engine:
            print('Средство передвижения едет.')

    def stop(self):
        if self.working_engine:
            self.working_engine = False
            print('Двигатель остановлен.')


class Tank(Vehicle):

    count_ammo = 10

    def move(self):
        if self.working_engine:
            print('Гусеницы заскрипели от движения.')
        else:
            print('Нужно завести двигатель.')

    def shoot(self):
        if self.count_ammo > 0:
            print('Танк выстрелил.')
            self.count_ammo -= 1
        else:
            print('Снаряды закончились.')

    # Дополнительно создал метод для проверки кол-ва снарядов.
    def check_ammo(self):
        print(f'Осталось {self.count_ammo} снарядов.')


class Car(Vehicle):

    fuel = 100

    def start(self):
        if self.fuel <= 0:
            print('Бензина нет.')

        if not self.working_engine:
            self.working_engine = True
            print('Двигатель машины заведён.')

    def move(self):
        if self.working_engine:
            self.fuel -= 10
            print('Машина поехала.')
        else:
            print('Машина не заведена.')

        if self.working_engine and self.fuel <= 0:
            self.working_engine = False
            print('Машина заглохла.')


class Boat(Vehicle):

    air_pressure = 100

    def start(self):
        if not self.working_engine:
            self.working_engine = True
            print('Мотор лодки гудит.')

        if self.air_pressure <= 0:
            self.working_engine = False
            print('Лодка тонет!')

    def move(self):
        if self.working_engine:
            self.air_pressure -= 10
            print('Лодка плывёт.')
        else:
            print('Мотор лодки не заведён.')


def main():
    tank1 = Tank()
    tank2 = Tank()
    # Проверим, как работает поле класса для каждого его экзамплера.
    tank1.check_ammo()
    tank2.check_ammo()
    tank1.shoot()
    tank1.check_ammo()
    tank2.check_ammo()


if __name__ == '__main__':
    main()
