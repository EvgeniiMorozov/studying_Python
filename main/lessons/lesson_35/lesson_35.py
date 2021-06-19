# Принципы SOLID

# S - Single Responsibility Principle (Принцип единственной ответственности)
# O - Open-Closed Principle (Принцип открытости - закрытости)
# L - Liskov Substitution Principle (Принцип подстановки [Барбары] Лисков)
# I - Interface Segregation Principle (Принцип разделения интерфейсов)
# D - Dependency Inversion Principle (Принцип инверсии зависимостей)


# S - Single Responsibility Principle (Принцип единственной ответственности)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#     def save_animal(self, animal):
#         # сохраняет animal в БД
#         ...

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#
# class AnimalBase:
#     def save_animal(self, animal):
#         # сохраняет animal в БД
#         ...


# O - Open-Closed Principle (Принцип открытости - закрытости)
# Открыт для расширения, закрыт для модификации.

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#
# animals = [Animal('cat'), Animal('dog'), Animal('cow'), Animal('mouse')]
#
#
# def get_animal_sound(animals: list[Animal]):
#     for animal in animals:
#         if animal.name == 'cat':
#             return 'meow'
#
#         elif animal.name == 'dog':
#             return 'bark'
#
#         elif animal.name == 'cow':
#             return 'moo'


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#     def get_animal_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__(name='cat')
#
#     def get_animal_sound(self):
#         return 'meow'
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(name='dog')
#
#     def get_animal_sound(self):
#         return 'bark'
#
#
# class Cow(Animal):
#     def __init__(self):
#         super().__init__(name='cow')
#
#     def get_animal_sound(self):
#         return 'moo'
#
#
# class Mouse(Animal):
#     def __init__(self):
#         super().__init__(name='mouse')
#
#     def get_animal_sound(self):
#         return 'pi pi pi'
#
#
# animals = [Cat(), Dog(), Cow(), Mouse()]
#
#
# def get_animal_sound(animals: list[Animal]):
#     for animal in animals:
#         animal.get_animal_sound()


# L - Liskov Substitution Principle (Принцип подстановки [Барбары] Лисков)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_animal_name(self):
#         return self.name
#
#
# class Cat(Animal):
#     def __init__(self):
#         super().__init__(name='cat')
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(name='dog')
#
#
# class Cow(Animal):
#     def __init__(self):
#         super().__init__(name='cow')
#
#
# def get_animal_legs(animals: list[Animal]):
#     for animal in animals:
#         pass


# I - Interface Segregation Principle (Принцип разделения интерфейсов)

# from abc import ABC, abstractmethod
#
#
# class IFigure(ABC):
#
#     @abstractmethod
#     def draw_circle(self):
#         pass
#
#     @abstractmethod
#     def draw_square(self):
#         pass
#
#     @abstractmethod
#     def draw_rectangle(self):
#         pass
#
#
# class Circle(IFigure):
#     def draw_circle(self):
#         pass  # реализация того, как рисуется круг


# class IFigure:
#     def draw(self):
#         pass
#
#
# class Circle(IFigure):
#     def draw(self):
#         print('Рисуем круг')
#
#
# class Square(IFigure):
#     def draw(self):
#         print('Рисуем квадрат')


# D - Dependency Inversion Principle (Принцип инверсии зависимостей)

# class ConsolePrinter:
#     def print(self):
#         pass
#
#
# class Book:
#     def __init__(self, txt):
#         self.text = txt
#         self.printer = ConsolePrinter()
#
#     def print(self):
#         self.printer.print()


class IPrinter:
    def print(self):
        pass


class ConsolePrinter(IPrinter):
    def print(self):
        print('Печатаем в консоль')


class UserPrinter(IPrinter):
    def print(self):
        print('Печатаем на бумаге')


class Book:
    def __init__(self, txt):
        self.text = txt
        self.printer: IPrinter = None

    def set_printer(self, printer: IPrinter):
        self.printer = printer

    def print(self):
        self.printer.print()


def main():
    pass


if __name__ == '__main__':
    main()
