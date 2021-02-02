# Строки

# words = 'Hello, world!'
# s = 'C:\d\new.txt'
# print(s)
# C:\d
# ew.txt

# s = r'C:\d\new.txt'  # объявили сырую строку - row string (не обрабатываются управляющие последовательности)
# print(s)
# # C:\d\new.txt

# Конкотенация строк

# s = 'Py' 'thon'
# print(s)  # Python

# s1 = 'Hello, '
# s2 = 'World!'
# s3 = s1 + s2
# print(s3)  # Hello, World!

# name = 'John'
# age = 20
# print('My name is ' + name)  # My name is John
# print('My name is ' + name + '.' + 'I`m' + age)
# произойдет ошибка: TypeError: can only concatenate str (not "int") to str
# В данном случаем, число надо привести к строке
# print('My name is ' + name + '. ' + 'I`m ' + str(age))  # My name is John. I`m 20

# Индексирование строк

# s = 'Hello world!'
# print(s[0])  # H
# print(s[12])  # обращение к несуществующему символу в этой строке IndexError: string index out of range
# print(s[-1])  # !
# print(s[-2])  # d
# print(s[-12])  # H

# Строки в питоне относятся к категории неизменяемых (immutable) последовательностей
# s[0] = 'D'  # ошибка - TypeError: 'str' object does not support item assignment

# Срезы
'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
 -12  -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''
# [X:Y:Z]
# X - начало среза (по умолчанию = 0)
# Y - конец среза (по умолчанию = длине строки)
# Z - шаг среза (по умолчанию = 1)
# если шаг задать -1 то строку можно перевернуть 'Hello world!' --> '!dlrow olleH'

# s = 'Hello world!'
# print(s[0:12])  # Hello world!
# print(s[::])  # Hello world!
# print(s[0:5])  # Hello
# print(s[:5])  # Hello
# print(s[6:])  # world!
# print(s[6::2])  # wrd
# print(s[::2])  # Hlowrd
# print(s[::3])  # Hlwl
# print(s[::-1])  # !dlrow olleH
# print(s[:5] + s[6:])  # Helloworld!

# Методы строк

# 1. Длина строки (это функция) len()

# s = 'hello'
# s1 = 'Привет'
# print(len(s))  # 5
# print(len(s1))  # 6

# str.capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний

# s = 'HELLO'
# print(s.capitalize())  # Hello
# print(s)  # HELLO

# str.center(width, [fill]) - Возвращает отцентрованную строку,
# по краям которой стоит символ fill (пробел по умолчанию)

# s = 'hello'
# print(s.center(20))  # '       hello        '
# print(s.center(20, '!'))  # !!!!!!!hello!!!!!!!!

# str.count(str, [start],[end]) - Возвращает количество непересекающихся
# вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)

# s = 'hello'
# print(s.count('l'))  # 2
# print(s.count('o'))  # 1
# print(s.count('a'))  # 0
# print(s.count('l', 0, 3))  # 1

# str.find(str, [start],[end]) - Поиск подстроки в строке.
# Возвращает номер первого вхождения или -1

# str.index(str, [start],[end]) - Поиск подстроки в строке.
# Возвращает номер первого вхождения или вызывает ValueError

# s = 'hello'
# print(s.find('l'))  # 2  - есть и её позиция 2
# print(s.find('o'))  # 4

# str.replace(шаблон, замена) - Замена шаблона

# s = 'hello'
# print(s.replace('l', 't'))  # hetto

# str.split([symbol]) - Разбиение строки по разделителю
# [symbol] - опциональный параметр (по-умолчанию пробел)

# s = 'hello world'
# print(s.split())  # ['hello', 'world']  - на выходе получим список
# print(s.split(','))  # ['hello world']

'''
str.isdigit() - Состоит ли строка из цифр (целиком)
str.isalpha() - Состоит ли строка из букв (целиком)
str.isalnum() - Состоит ли строка из цифр или букв
str.islower() - Состоит ли строка из символов в нижнем регистре
str.isupper() - Состоит ли строка из символов в верхнем регистре
'''

# s = 'hello, world'
#
# print(s.isdigit())  # False
# print(s.isalpha())  # False (потому, что есть запятая и пробел)

