# Занятие 18. ООП. Решение задач, UML, Ассоциации

# http://old.code.mu/tasks/php/oop/osnovy-raboty-s-objektno-orientirovannym-programmirovaniem-v-php-1.html

# Сделайте класс User, в котором будут следующие protected поля - name (имя), age (возраст),
# public методы setName, getName, setAge, getAge.
#
# Сделайте класс Worker, который наследует от класса User и вносит дополнительное private поле salary (зарплата),
# а также методы public getSalary и setSalary.
#
# Создайте объект этого класса 'Иван', возраст 25, зарплата 1000. Создайте второй объект этого класса 'Вася',
# возраст 26, зарплата 2000. Найдите сумму зарплата Ивана и Васи.
#
# Сделайте класс Student, который наследует от класса User и вносит дополнительные private поля стипендия,
# курс, а также геттеры и сеттеры для них.

class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise ValueError('Передан неверный тип значения')

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Worker(User):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f'Работник {self.get_name()} возрастом {self.get_age()} лет, зарплатой {self.get_salary()} рублей.'


class Student(User):

    def __init__(self, name, age, scholarship, course):
        super().__init__(name, age)
        self.__scholarship = scholarship
        self.__course = course

    def get_scholarship(self):
        return self.__scholarship

    def set_scholarship(self, scholarship):
        self.__scholarship = scholarship

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def __str__(self):
        return f'Студент {self.get_name()},' \
               f' курс {self.get_course()},' \
               f' возрастом {self.get_age()} лет,' \
               f' стипендия: {self.get_scholarship()}'


# https://www.cyberforum.ru/cpp-beginners/thread623309.html
'''
 Класс Дробное число со знаком (Fractions). Число должно быть представлено двумя полями:
 целая часть - длинное целое со знаком, дробная часть - беззнаковое короткое целое.
 Реализовать арифметические операции сложения, вычитания, умножения и операции сравнения.
В функции main проверить эти методы.
'''


class FractionNum:
    def __init__(self, dec, frac):
        self.decimal = dec
        self.fraction = frac

    def __str__(self):
        return f'{self.decimal}.{self.fraction}'

    def __add__(self, other):
        dec = self.decimal + other.decimal
        frac = self.fraction + other.fraction

        if frac > 100:
            buffer = frac // 100
            dec += buffer
            frac %= buffer * 100

        return FractionNum(dec, frac)

    def __sub__(self, other):
        dec = self.decimal - other.decimal
        frac = self.fraction - other.fraction

        if frac > 100:
            dec -= 1
            frac = abs(100 - frac)

        return FractionNum(dec, frac)


def main():
    # user1 = Worker('Иван', 25, 1000)
    # user2 = Worker('Вася', 26, 2000)
    #
    # print(user1)
    # print(user2)
    #
    # student1 = Student('Михаил', 19, 5000, 1)
    # student2 = Student('Олег', 21, 7000, 3)
    #
    # print(student1)
    # print(student2)

    num1 = FractionNum(1, 25)
    num2 = FractionNum(-12, 70)

    print(num1)
    print(num2)
    print(num1 - num2)


if __name__ == '__main__':
    main()
