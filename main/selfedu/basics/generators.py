# https://www.youtube.com/watch?v=VxLzxh9B8EE&ab_channel=selfedu

# a = [1, 2, 3]
# it = iter(a)  # итератор - это объект, который поддерживает next() для перехода к след элементу коллекции.
# print(it)  # <list_iterator object at 0x0000024FE4844FD0>

# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # error: StopIteration

# b = (x**2 for x in range(10))
# b - итератор
# (x**2 for x in range(10)) - выражение-итератор

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# print(next(b))

# Генератор не хранит в памяти все значения, как списки, а генерирует их по мере необходимости.

# print(list(range(1000000000000000)))  # MemoryError
# print((x for x in range(1000000000000000)))  # <generator object <genexpr> at 0x000001C80EE4D740>

# lst = (x for x in range(1000000000000000))
# for i in lst:
#     print(i, end=' ')
#     if i > 100:
#         break
# 0 1 2 3 4 5 6 7 8 9 10 ..... 91 92 93 94 95 96 97 98 99 100 101

# print('\nNew Loop')
#
# for i in lst:
#     print(i, end=' ')
#     if i > 200:
#         break
# 102 103 104 105 106 107 108 ...... 193 194 195 196 197 198 199 200 201

# Переменные используются 1 раз !!!

# Функции - генераторы


def get_all_average(N):
    avs = []
    count = 0
    S = 0
    for i in range(1, N+1):
        count += 1
        S += i
        avs.append(S/count)

    return avs


def get_all_average_1(N):
    count = 0
    S = 0
    for i in range(1, N+1):
        count += 1
        S += i
        yield S/count


print(get_all_average(100))
print(get_all_average(100).__sizeof__())  # 904

it = get_all_average_1(10)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


# def f():
#     return list(range(10))
#
#
# print(f())  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def f():
#     for x in range(10):
#         yield x
#
#
# s = f()
# print(s)  # <generator object f at 0x000001C72928D820>
#
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
