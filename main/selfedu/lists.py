# Lists ( списки )

# Создание списков

# 1. Задать через квадратные скобки []
# l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]

# print(type(l1))  # <class 'list'>
# print(l1)  # [1, 2, 3, 'hello', ['test', 10], 'world', True]

# 2. с помощью функции list, передав её на вход иттерируемую последовательность

# l2 = list('hello')  # на вход list передали иттерируемую последовательность

# print(l1, l2, sep='\n')
# [1, 2, 3, 'hello', ['test', 10], 'world', True]
# ['h', 'e', 'l', 'l', 'o']

# l3 = list((1, 2, 3))  # (1, 2, 3) - кортеж

# print(l1, l2, l3, sep='\n')
# [1, 2, 3, 'hello', ['test', 10], 'world', True]
# ['h', 'e', 'l', 'l', 'o']
# [1, 2, 3]

# 3. использовать "генератор списков" (функция range или цикл for)

# l4 = [i for i in 'world']
# print(l1, l2, l3, l4, sep='\n')
# [1, 2, 3, 'hello', ['test', 10], 'world', True]
# ['h', 'e', 'l', 'l', 'o']
# [1, 2, 3]
"""
Преимуществом генератора списка над функцией list является то, что в процессе
генерации списка, мы можем совершать действия над ним.
"""

# l5 = [i for i in 'hello world' if i != ' ']

# print(l5)
# ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']  - в процессе сборки списка убрали пробел

# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
# print(l5)
# ['h', 'l', 'l', 'w', 'r', 'l', 'd']  - убрали пробелы и гласные буквы
# l5 = [i*2 for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
# print(l5)
# ['hh', 'll', 'll', 'ww', 'rr', 'll', 'dd'] - отсортировали согласные и продублировали их

# print(range(10))  # range(0, 10)
# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1, 11)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(range(0, 11, 2)))  # [0, 2, 4, 6, 8, 10]

# l6 = list(range(0, 11))
# print(l6)

# for i in range(1, 3):
#     print(f'внешний цикл #{i}')
#     for j in range(1, 3):
#         print(f'\tвнутренний цикл #{j}')

# внешний цикл #1
# 	внутренний цикл #1
# 	внутренний цикл #2
# внешний цикл #2
# 	внутренний цикл #1
# 	внутренний цикл #2

# Методы работы со списками

"""
list.append(x) - Добавляет элемент в конец списка.

list.extend(L) - Расширяет список list, добавляя в конец все элементы списка L.

list.insert(i, x) - Вставляет на i-ый элемент значение x.

list.remove(x) - Удаляет первый элемент в списке, имеющий значение x.
ValueError, если такого элемента не существует.

list.pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан,
удаляется последний элемент.

list.index(x, [start [, end]]) - Возвращает положение первого элемента со
значением x (при этом поиск ведется от start до end).

list.count(x) - Возвращает количество элементов со значением x.

list.sort([key=функция], [reverse=False]) - Сортирует список на основе функции.

list.reverse() - Разворачивает список.

list.copy() - Возвращает копию списка.

list.clear() - Очищает список.
"""

l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Ivanov', 'Petrov', 'Sidorov']

# print(l1[3])  # hello
# print(l1[4][0])  # test

# срез

# print(l1[0:3])  # [1, 2, 3]

# изменяемость списков

# print(l1)  # [1, 2, 3, 'hello', ['test', 10], 'world', True]
l1[2] = 'world'
# print(l1)  # [1, 2, 'world', 'hello', ['test', 10], 'world', True]
# l1[:2] = [10, 15]
# print(l1)  # [10, 15, 'world', 'hello', ['test', 10], 'world', True]

# list.append()

l1.append('new')
# print(l1)  # [1, 2, 'world', 'hello', ['test', 10], 'world', True, 'new']

# list.extend()

l1.extend([5, 7])
# print(l1)  # [1, 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7]

l2 = ['hi', 19]
l1 += l2
# print(l1)  # [1, 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]

# list.insert()

l1.insert(1, 'test')
# print(l1)  # [1, 'test', 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]

# list.remove()

# l1.remove('world')
# print(l1)  # [1, 'test', 2, 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]

# list.pop()

# el = l1.pop()
# print(l1, el, sep='\n')
# [1, 'test', 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi']
# 19

# el = l1.pop(1)
# print(l1, el, sep='\n')
# [1, 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]
# test

# list.count()

# print(l1, l1.count('world'), sep='\n')
# [1, 'test', 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]
# 2
# print(l1, l1.count('test'), sep='\n')
# [1, 'test', 2, 'world', 'hello', ['test', 10], 'world', True, 'new', 5, 7, 'hi', 19]
# 1

# list.sort()

# l1.sort()
# print(l1)  # TypeError: '<' not supported between instances of 'str' and 'int'
# метод sort будет работать со списком, только если там элементы одного типа данных

l3 = ['hello', 'hi', 'David', 'world', 'test']
print(l3)  # ['hello', 'hi', 'David', 'world', 'test']
l3.sort()
print(l3)  # ['David', 'hello', 'hi', 'test', 'world']



