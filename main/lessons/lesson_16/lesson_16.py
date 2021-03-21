import turtle


# Введение в ООП.
class Car:
    count = 0  # аттрибут класса (общий для всех экземпляров класса)

    # Конструктор объекта, экземпляра (вызывается при создании объекта)
    def __init__(self, mark, wheels, speed):
        Car.count += 1
        self.mark = mark  # переменные, поля, аттрибуты
        self.wheels = wheels
        self.speed = speed

    # Функции, определённые внутри класса называются методами класса(объекта).
    def drive(self):
        print(f'{self.mark} едет со скоростью {self.speed}')

    # Получает доступ к данным экземпляра (instance-метод)
    def set_speed(self, speed):
        self.speed = speed

    # Получает доступ к данным ВСЕГО класса
    @classmethod
    def get_count_cars(cls):
        print(f'Количество оставшихся машин: {cls.count}')

    # Не получает доступ к данным экземпляра, но существует внутри его для удобства
    @staticmethod
    def print_hi():
        print(f'Машина говорит привет!')

    # Деструктор (вызывается, когда объект прекращает свою жизнь)
    def __del__(self):
        Car.count -= 1
        print(f'{self.mark} разбилась со скоростью {self.speed}. Осталось машин: {Car.count}')


class Animals:

    def move(self):
        print('Животное передвигается.')

    def eat(self):
        print('Животное ест.')


# потомок класса Animals
class Insects(Animals):

    def rit_noru(self):
        print('Насекомое роёт нору')

    def eat(self):
        print('Насекомое ест листья и насекомых')


class Fish(Animals):

    def __init__(self):
        __var = 1

    def play_in_water(self):
        print('Рыба играет в воде')

    def barahtatsya_in_water(self):
        print('Рыба барахтается в воде')

    def eat(self):
        print('Рыба ест планктон')

    def __live_in_leaves(self):
        print('Рыба живёт в водорослях')


class Shark(Fish):
    def broke_smth_via_tooth(self):
        print('Акула что-то ломает зубами')

    def eat(self):
        print('Акула ест других рыб')


class Mammals(Animals):

    def feed_milk(self):
        print('Млекопитающие поят молоком')

    def barahtatsya_in_water(self):
        print('Млекопитающее барахтается в воде')

    def eat(self):
        print("Млекопитающее ест траву")


# Множественное наследование
class Dolphin(Mammals, Fish):
    def smth(self):
        Fish.barahtatsya_in_water(self)

    def eat(self):
        print('Дельфин есть планктон')


# Научно-технический рэп - Полиморфизм


def main():
    # car1 = Car('Toyota', 4, 60)  # Объект, экземпляр, instance
    # car2 = Car('Bentley', 4, 80)  # Другой объект, экземпляр, instance
    # Это как бы свой тип данных
    # print(type(car1))

    # Все объекты независимы
    # print(car1.mark)  # Toyota
    # print(car2.mark)  # Bentley

    # Методы объектов
    # car1.drive()
    # car1.set_speed(70)
    # car1.drive()
    #
    # car2.drive()
    # car2.set_speed(40)
    # car2.drive()
    #
    # Car.get_count_cars()

    # del car1
    # car1.drive()

    # Наследование, Полиморфизм, Инкапсуляция и иногда Абстракция.

    # Наследование.
    # Животные могут передвигаться и бегать, но такое разделение слишком общее
    # animal1 = Animals()
    # animal2 = Animals()
    #
    # # Добавили насекомых
    # insect1 = Insects()
    # insect2 = Insects()
    #
    # insect1.move()
    # insect2.eat()
    #
    # fish1 = Fish()
    # # fish1._broke_smth_via_tooth()  # нет такой возможности у рыб, зато есть у акул
    # shark1 = Shark()
    # shark1.broke_smth_via_tooth()

    # создадим дельфина
    # dolphin1 = Dolphin()
    # dolphin1.feed_milk()
    # dolphin1.play_in_water()
    # dolphin1.barahtatsya_in_water()
    # dolphin1.smth()

    # Полиморфизм
    # insect1 = Insects()
    # shark1 = Shark()
    # mammal1 = Mammals()
    # dolphin1 = Dolphin()
    #
    # insect1.eat()
    # shark1.eat()
    # mammal1.eat()
    # dolphin1.eat()
    #
    # # Инкапсуляция
    # # Public - публичный доступ
    # # Protected - защищённый доступ (_method)
    # # Private - привытный доступ (__method)
    #
    # # shark1.__live_in_leaves()
    # fish1 = Fish()
    # # fish1.__live_in_leaves()
    # fish1.__var = 2
    # print(fish1.__var)

    turtle1 = turtle.Turtle('red')
    turtle2 = turtle.Turtle('blue')

    turtle1.circle(100)

    for _ in range(4):
        turtle2.forward(50)
        turtle2.right(90)


if __name__ == '__main__':
    main()
