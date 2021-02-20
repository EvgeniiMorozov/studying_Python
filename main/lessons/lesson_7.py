import time
from math import sqrt
from functools import reduce


# Вариант решения домашнего задания
def exact_degree_two_1(num):
    if num == 1:
        print('Yes')
        return
    elif num < 1:
        print('No')
        return
    exact_degree_two_1(num/2)


def get_num(n):
    for i in range(n):
        print(n)


def get_rec_num(x, n):
    if x == n:
        return
    print(x)
    get_rec_num(x+1, n)


# Функциональное программирование
# умножение
def mul(a):
    def inner_mul(b):
        return a * b
    return inner_mul


# замыкание
def func1(a):
    x = a**2

    def inner_func():
        return x + 10

    return inner_func()


def to_meters(km):
    return km * 1000


def to_cms(m):
    return m * 100


def to_mm(cm):
    return cm * 10


def get_mms(km):

    def _to_meters(km):
        return km * 1000

    def _to_cms(m):
        return m * 100

    def _to_mms(cm):
        return cm * 10

    return _to_mms(_to_cms(_to_meters(km)))


# Каррирование
def transform(b, c, d):
    def a(x):
        return b(c(d(x)))
    return a


def days_to_hours(days):
    return days * 24


def hours_to_minutes(hours):
    return hours * 60


def minutes_to_seconds(minutes):
    return minutes * 60


# foo1(x)(y1)(y2)(z)
def z(num):
    return num


def y2():
    return z


def y1():
    return y2


def x():
    return y1


# Декораторы
def decorator (func):
    def inner_wrapper():
        print('Декоратор начался')
        func()
        print('Декоратор закончился')
    return inner_wrapper


def simple_func():
    print('Simple function')


def get_exec_time(func):
    def inner_wrapper(*args):
        start_time = time.time()
        func(*args)
        print(f'Функция {func.__name__} выполнено за {time.time() - start_time:.2} сек.')
    return inner_wrapper


@get_exec_time
def hard_func(N):
    sum = 0
    for i in range(N+1):
        sum += i
    print(f'Сумма {N} чисел равна: {sum}')


# Решение задач
# даны катеты прямоугольного треугольника, найти S, P и гипотенузу
def triangle_stats(cat1, cat2):
    def _square():
        return cat1 * cat2 / 2

    def _perimetr():
        return cat1 + cat2 + _hyp()

    def _hyp():
        return sqrt(cat1**2 + cat2**2)

    print(f'Треугольник со сторонами {cat1} {cat2} {_hyp()}')
    print(f'Площадь {_square()} | Периметр {_perimetr()}')


# в массиве замените все числа, большие данного числа, на среднее арифметическое всех чисел массива
def replace_nums(arr, number):
    def _mean():
        return reduce(lambda x, y: x + y, arr) / len(arr)

    # def _is_greater_then_mean(num):
    #     return True if num > number else False

    # def _replace(num):
    #     return _mean() if _is_greater_then_mean(num) else num

    def _is_greater_then_mean():
        return list(filter(lambda x: x > number, arr))

    def _replace(num):
        return _mean() if num in _is_greater_then_mean() else num

    return list(map(_replace, arr))


def main():
    # get_rec_num(1, 10)
    # exact_degree_two_1(1023)

    # print(mul(5)(10))
    # print(func1(10))

    # print(to_mm(to_cms(to_meters(1))))
    # print(get_mms(1))

    # каррирование
    # print(minutes_to_seconds(hours_to_minutes(days_to_hours(1))))
    # days_to_seconds = transform(minutes_to_seconds, hours_to_minutes, days_to_hours)
    # print(days_to_seconds(1))

    # foo1 = x()()()(5)
    # print(foo1)

    # Декоратор
    # dec = decorator(simple_func)
    # dec()
    # start_time = time.time()
    # hard_func(100000000)
    # print(f'Выполнено за {time.time() - start_time:.2} сек.')
    # hard_func(10000000)

    # Решение задач
    # triangle_stats(3, 4)
    print(replace_nums([1, 2, 3, 4, 5], 1))


if __name__ == '__main__':
    main()
