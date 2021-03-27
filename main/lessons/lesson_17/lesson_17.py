# Занятие 17. ООП. Задачи, наследование, super, magic
# class B:
#     three = 3
#
#     def __init__(self):
#         self.two = 2
#
#
# class A(B):
#     def __init__(self):
#         super().__init__()
#         self.one = 1


class Tank:

    def __init__(self):
        self.count_ammo = 10

    def shoot(self):
        self.count_ammo -= 1


class TigerTank(Tank):
    def __init__(self):
        super(TigerTank, self).__init__()
        self.speed = 100


class Base:

    def price(self):
        return 10


class Discount(Base):

    def __init__(self):
        self.cost = 8

    def price(self):
        return super(Discount, self).price() * self.cost


class O:
    def method(self):
        print('I`m O')


class A(O):
    def method(self):
        super().method()
        # O.method(self)
        print('I`m A')


class B(O):
    def method(self):
        super().method()
        print('I`m B')


# class D(O):
#     def method(self):
#         super().method()
#         print('I`m D')


class C(A, B):
    def method(self):
        super(A, self).method()
        # A.method(self)
        print('I`m C')


class Car:
    def __init__(self, mark, speed):
        self.mark = mark
        self.speed = speed

    def __gt__(self, other):
        # return self.speed > other.speed
        return f'{self.mark} круче' if self.speed > other.speed else f'{self.mark} хуже'

    def __eq__(self, other):
        return self.speed == other.speed

    def __ge__(self, other):
        return self.speed >= other.speed

    def __neg__(self):
        return -self.speed

    def __abs__(self):
        return abs(self.speed)

    def __str__(self):
        return f'{self.__class__} Машина {self.mark} | Скорость: {self.speed}'


class Worker:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


class Crocodile:
    def __init__(self, legs, name):
        self.legs = legs
        self.name = name

    # def to_car(self):
    #     return Car()


def main():
    # a = A()
    # print(a.one)
    # print(a.two)
    # print(a.three)

    # tank1 = Tank()
    # tank2 = Tank()
    # print(tank1.count_ammo)
    # print(tank2.count_ammo)
    #
    # tank1.shoot()
    # print(tank1.count_ammo)
    # print(tank2.count_ammo)

    # tiger = TigerTank()
    # print(tiger.count_ammo)

    # dsc = Discount()
    # print(dsc.price())

    # c = C()
    # c.method()

    # a = A()
    # a.method()

    # car1 = Car('Toyota', 120)
    # car2 = Car('Mercedes', 140)
    #
    # print(car1)
    # print(car2)
    # print(car1 > car2)
    # print(-car1)

    ivan = Worker('Ivan', 25, 2000)
    vasya = Worker('Vasya', 31, 100000)
    print(ivan.age + vasya.age)
    print(ivan.salary + vasya.salary)


if __name__ == '__main__':
    main()
