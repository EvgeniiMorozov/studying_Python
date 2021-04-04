# Занятие 20. ООП. Практика решения задач

# Task_1
"""
Создайте класс с именем student, содержащую поля: фамилия и инициалы, номер группы,
успеваемость (массив из пяти элементов). Создать массив из десяти элементов такого типа, упорядочить записи по
возрастанию среднего балла. Добавить возможность вывода фамилий и номеров групп студентов,
имеющих оценки, равные только 4 или 5.
"""


class Student:
    def __init__(self, lastname, group, marks):
        self.lastname: str = lastname
        self.group = group
        self.marks: list = marks

    def mean_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @staticmethod
    def get_good_students():
        good_lst = list(filter(lambda x: x != 2 and x != 3, Student.marks))

    def __str__(self):
        return f'Студент: {self.lastname} | Средний балл: {self.mean_mark()}'

    def __repr__(self):
        return f'Студент: {self.lastname} | Средний балл: {self.mean_mark()}'

    # def __lt__(self, other):
    #     return self.mean_mark() < other.mean_mark()

"""
Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу
в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
Написать программу, демонстрирующую все возможности класса.
"""


class Counter:

    def __init__(self, min_value, max_value, current_value=0):
        self.current_value = current_value
        self.__min_value = min_value
        self.__max_value = max_value

    def increase_value(self):
        self.current_value += 1
        self.__check_counter()

    def decrease_value(self):
        self.current_value -= 1
        self.__check_counter()

    def __check_counter(self):
        if self.current_value > self.__max_value:
            self.current_value = self.__min_value
        elif self.current_value < self.__min_value:
            self.current_value = self.__max_value


# Task_3
"""
Построить три класса (базовый и 3 потомка), описывающих некоторых хищных животных (один из потомков),
всеядных(второй потомок) и травоядных (третий потомок). Описать в базовом классе абстрактный метод для расчета
количества и типа пищи, необходимого для пропитания животного в зоопарке.
a) Упорядочить всю последовательность животных по убыванию количества пищи. При совпадении значений – упорядочивать
данные по алфавиту по имени. Вывести идентификатор животного, имя, тип и количество потребляемой
пищи для всех элементов списка.
b) Вывести первые 5 имен животных из полученного в пункте а) списка.
c) Вывести последние 3 идентификатора животных из полученного в пункте а) списка.
d) Организовать запись и чтение коллекции в/из файл.
e) Организовать обработку некорректного формата входного файла.
"""


class Animal:
    def __init__(self, name, food_amount, food_type):
        self.name = name
        self.food_type = food_type
        self.food_amount = food_amount

    def calculate_food(self, days: int):
        raise NotImplemented

    def __lt__(self, other):
        return self.food_amount < other.food_amount

    def __repr__(self):
        return f'Животное {self.name}, ест {self.food_type} в кол-ве {self.food_amount} кг'


class Carnivore(Animal):
    def __init__(self, name, food_amount, food_type='мясо'):
        super(Carnivore, self).__init__(name, food_amount, food_type)

    def calculate_food(self, days: int):
        return self.food_amount * 3 * days


class Herbivore(Animal):
    def __init__(self, name, food_amount, food_type='растительность'):
        super(Herbivore, self).__init__(name, food_amount, food_type)

    def calculate_food(self, days: int):
        return self.food_amount * 5 * days


class Omnivore(Animal):
    def __init__(self, name, food_amount, food_type='всё'):
        super(Omnivore, self).__init__(name, food_amount, food_type)

    def calculate_food(self, days: int):
        return self.food_amount * 2 * days


def main():
    # Task_1
    # list_of_students = []
    # list_of_lastnames = [
    #     'Vasya I. V.',
    #     'Ivan K. O.',
    #     'Petr B. V.',
    #     'Nikolay I. V.',
    #     'Oleg I. D.'
    # ]
    # list_of_groups = [1, 2, 3, 4, 5]
    # list_of_marks = [
    #     [3, 4, 5, 4, 3, 5, 3],
    #     [3, 3, 3, 3, 3, 4, 5],
    #     [5, 5, 5, 5, 5, 5, 5],
    #     [4, 4, 4, 4, 4, 4, 4],
    #     [2, 3, 3, 3, 3, 2, 2]
    # ]
    # for i in range(5):
    #     list_of_students.append(Student(list_of_lastnames[i], list_of_groups[i], list_of_marks[i]))
    #
    # print(list_of_students)
    # print(list_of_students[0])
    #
    # print(sorted(list_of_students, key=Student.mean_mark))

    # Task_2
    counter1 = Counter(1, 5, 2)

    # print(counter1.current_value)
    # counter1.increase_value()
    # counter1.increase_value()
    # counter1.increase_value()
    # print(counter1.current_value)
    # counter1.increase_value()
    # print(counter1.current_value)

    # Task_3

    carnivore1 = Carnivore('Акелла', 5)
    carnivore2 = Carnivore('Табаки', 3)
    carnivore3 = Carnivore('Шер-Хан', 6)

    herbivore1 = Herbivore('Рубин', 7)
    herbivore2 = Herbivore('Стрелка', 4)
    herbivore3 = Herbivore('Бемби', 2)

    omnivore1 = Omnivore('Снежок', 7)
    omnivore2 = Omnivore('Барсик', 4)
    omnivore3 = Omnivore('Кеша', 2)

    all_list = [carnivore1, carnivore2, carnivore3, herbivore1, herbivore2, herbivore3, omnivore1, omnivore2, omnivore3]

    for animal in sorted(all_list, reverse=True):
        print(animal)


if __name__ == '__main__':
    main()
