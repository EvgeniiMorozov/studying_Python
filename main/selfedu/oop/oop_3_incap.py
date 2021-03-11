from classes import Person

person1 = Person('John')
# person1.print_info()
# Name: John, Age: 20

person2 = Person('Katy')
# person2._age = 30
# person2.print_info()
# Name: Katy, Age: 30

# Полной инкапсуляции в питоне нет!

# Получение закрытого свойства
# print(person2._Person__age)  # 20

# Геттеры и сеттеры
# print(person2.get_age())  # 20
# person2.set_age(25)
# person2.print_info()  # Name: Katy, Age: 25

print(person2.age)  # <bound method Person.age of <classes.Person object at 0x7fa13e3c1d00>>
person2.age = 35
person2.print_info()  # Name: Katy, Age: 35


