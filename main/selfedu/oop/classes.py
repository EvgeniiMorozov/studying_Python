# class Person:
#     # name = 'John'
#
#     def __init__(self, name):
#         print('Hi')
#         self.name = name
#
#     def print_info(self):
#         print(f'Hello, my name is {self.name}')

class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 20
        # _var - соглашение о защищенной переменной
        # __var - приватное свойство

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('wrong age!')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('wrong age!')



