# Множества
"""
По сути множества, это неупорядочненная коллекция элементов,
и отсюда вытекает, что множества не поддерживают индексирование.
"""

# Создание множества

# 1. литерал множества

# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# print(type(s))  # <class 'set'>
# print(s)  # {'pear', 'banana', 'apple', 'orange'}
# {'apple', 'orange', 'banana', 'pear'}
# {'pear', 'apple', 'banana', 'orange'}

# дубли были удалены

# 2. с помощью конструктора set

# s2 = set('hello')
# print(s2)  # {'o', 'h', 'l', 'e'}

# 3. использовать генератор

# s3 = {i for i in range(1, 11)}
# print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# s4 = {2, 1, 3, 4, 7, 6, 5, 8, 10, 9}
# print(s4)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# создание пустого множества

# !!!!!! при использовании пустых фигурных скобок, создаётся словарь
# print(type({}))  # <class 'dict'>

# s4 = set()
# print(type(s4))  # <class 'set'>

"""
Множества удобно использовать для удаления дубликатов из списков.
"""
# nums = [1, 2, 3, 3, 1, 2, 4, 5]
# nums2 = set(nums)
# print(nums2)  # {1, 2, 3, 4, 5}
# nums2 = list(set(nums))
# print(nums2)  # [1, 2, 3, 4, 5]

# Операции над множествами

a = set('abracadabra')
b = set('alacazam')

# print(a, b, sep='\n')
# {'b', 'c', 'd', 'r', 'a'}
# {'m', 'c', 'z', 'l', 'a'}

c = a - b  # вычитание - убираем из a все буквы, которые есть в b
# print(c)  # {'r', 'b', 'd'}

d = a | b  # объединение - буквы или в a или в b
# print(a, b, d, sep='\n')
# {'c', 'b', 'r', 'd', 'a'}
# {'l', 'm', 'z', 'c', 'a'}
# {'l', 'm', 'z', 'r', 'b', 'c', 'd', 'a'}

e = a & b  # пересечение - буквы и в a и в b
# print(a, b, e, sep='\n')
# {'d', 'a', 'r', 'b', 'c'}
# {'l', 'm', 'a', 'z', 'c'}
# {'c', 'a'}

f = a ^ b  # множество из элементов - буквы в a или b, но не в обоих
# print(a, b, f, sep='\n')
# {'b', 'a', 'r', 'c', 'd'}
# {'a', 'z', 'c', 'm', 'l'}
# {'z', 'm', 'r', 'b', 'd', 'l'}

"""
Методы работы с множествами.

set.copy() - возвращает копию множества.

set.add(elem) - добавляет элемент в множество.

set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.

set.discard(elem) - удаляет элемент, если он находится в множестве.

set.pop() - возвращает и удаляет первый элемент из множества.
Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.

set.clear() - очистка множества.
"""

s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s.copy()
# print(s, id(s))
# print(s2, id(s2))
# {'pear', 'apple', 'orange', 'banana'} 3168768122208
# {'pear', 'apple', 'orange', 'banana'} 3168768122432

# s.add('melon')
# print(s)
# {'pear', 'orange', 'apple', 'banana', 'melon'}

# s.clear()
# print(s)  # set()

# frozenset ( immutable set )

a = frozenset('hello')
print(a)  # frozenset({'e', 'l', 'o', 'h'})

# a.add('test')
# print(a)  # AttributeError: 'frozenset' object has no attribute 'add'




