# Tuples ( кортежи )
# immutable
# грубо говоря "неизменяемый" список

# создание кортежа

# литерал кортежа
# t1 = (1, 2, 3)  # tuple (кортеж)
# l1 = [1, 2, 3]  # list
#
# print(type(t1))  # <class 'tuple'>

# упаковка кортежа

# t1 = 1, 2, 3
# print(t1)  # (1, 2, 3)

# использование конструктора tuple

# t1 = tuple((1, 2, 3))
# print(t1)  # (1, 2, 3)

# создание пустого кортежа

# t1 = ()

# t1 = (1)
# print(t1)  # 1
# чтоб создать кортеж с 1м элементом, надо после него поставить запятую

# t1 = (1,)
# print(t1)  # (1,)

# t1 = tuple('hello')
# print(t1)  # ('h', 'e', 'l', 'l', 'o')

# t1 = (1, 2, 3)
# l1 = [1, 2, 3]
# print(t1.__sizeof__())  # 48 - кортеж занимает 48 байтов в памяти
# print(l1.__sizeof__())  # 104 - список занимает 104 байта в памяти
# кортеж занимает меньший объём памяти, чем список

# Операции над кортежами

# по сути, это те же операции, что и операции, производимые над списками, кроме тех,
# которые могут их изменять

# t1 = tuple('hello')
# t2 = tuple(' world')
# t3 = t1 + t2
# print(t3)
# ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')

# print(len(t3))  # 11

# print(t3.count('l'))  # 3
# print(t3.count('a'))  # 0

# print(t3.index('l'))  # 2
# print(t3.index('o'))  # 4
# print(t3.index('a'))  # ValueError: tuple.index(x): x not in tuple

# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print('No')
# No

# кортеж можно перебрать
# for i in t3:
#     print(i, end=' ')
# h e l l o   w o r l d

# for i in t3:
#     if i == ' ':
#         continue
#     print(i, end=' ')
# h e l l o w o r l d

# for i in t3:
#     if i == ' ':
#         continue
#     print(f'"{i}"', end=' ')
# "h" "e" "l" "l" "o" "w" "o" "r" "l" "d"

# внутрь кортежа можно вложить изменяемые элементы

# t1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world']) 2691149382176
# t1[0] = 'new'  # TypeError: 'tuple' object does not support item assignment

# t1[4][0] = 'new'
# print(t1, id(t1))
# (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world']) 2241424441888
# (10, 11, [1, 2, 3], [4, 5, 6], ['new', 'world']) 2241424441888
# t1[4].append('hello')
# print(t1, id(t1))
# (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world']) 2351848276512
# (10, 11, [1, 2, 3], [4, 5, 6], ['new', 'world']) 2351848276512
# (10, 11, [1, 2, 3], [4, 5, 6], ['new', 'world', 'hello']) 2351848276512


# распаковка кортежа

t1 = (1, 2, 3,)
# x = t1[0]
# y = t1[1]
# z = t1[2]
#
# print(x, y, z)  # 1 2 3

# x, y, z = t1  # распаковка кортежа
# print(x, y, z)  # 1 2 3

# x, y = t1  # ValueError: too many values to unpack (expected 2)

# x = 1
# y = 2
# print(x, y)  # 1 2
# x, y = y, x
# print(x, y)  # 2 1




