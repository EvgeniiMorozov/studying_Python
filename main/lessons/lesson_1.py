print('Hello, World!')

a = 5 # integer - целочисленный тип данных
print(a)

a = 'Hello' # string - строковый тип данных
print(a)

# вещественный тип данных float
a = 0.554547874
print(a)

# Математические операции
a = 5
b = 1
c = a + b
print('Результат:', c)
print('Результат:', a + b)

# Интересная штука с числами и строками
# a = 1 # integer
# b = '1' # string
# c = a + b
# print('Result:', c)

# Умножение строк
a = 5
b = 'строка'
c = b * a
print('Result (string * int):', c)

# Приведение типов

a = 1
b = '1'
c = a + int(b)
print('Result:', c)

# Пользовательский ввод
# a = input('Ввведите а: ')
# b = input('Ввведите b: ')
# c = a + b
# print('Result (input):', c)  # 2345000
# # input на выходе всегда string

# a = int(input('Ввведите а: '))  # 234
# b = int(input('Ввведите b: '))  # 5000
# c = a + b
# print('Result (input):', c)  # 5234

# проверка типа
a = 5
b = '5'
c = 5.0
print('Тип a:', type(a), 'Тип b:', type(b), 'Тип c:', type(c))

# приоритеты операторов
c = 1 + 2 * 3 / 5 - 10 + 10
print(c)

# ошибка в операциях с точкой
a = 1
b = 3
print('Делим 1 на 3:', a / b)

# Исключения

# Type error - произошла несостыковка с типами данных
# Value error -
# zero division error - деление на нуль
# syntax error
# Logical error
