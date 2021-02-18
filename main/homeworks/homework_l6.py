# Морозов Е.И. группа: Python026
from functools import reduce
from random import randint


# Задача 1 (на reduce и filter).
# Найдите сумму нечетных чисел массива, которые не превосходят 11.

# При решении этой задачи, необходимо задать два условия в лямбда-функции
# в filter() через логический оператор and: элемент списка меньше либо равен 11
# и остаток от деления на 2 не равен 0.

def sort_sum(arr: list[int]) -> int:
    """
    Определяет сумму нечетных чисел массива, которые не превосходят 11.

    :param arr: исходный массив натуральных чисел.
    :return: int
    """
    return reduce(lambda x, y: x+y, list(filter(lambda x: x <= 11 and x % 2 != 0, arr)))


# Вспомогательная функция для генерации списка из натуральных чисел.
def list_of_integers(n: int) -> list[int]:
    """
    Генерирует список из натуральных чисел.

    :param n: количество элементов списка.
    :return: list[int]
    """
    return [randint(0, 20) for _ in range(n)]


# Задача 2 (на map).
# На вход подаётся массив из строк. Требуется перевести каждый
# первый символ строки в верхний регистр.
def capitalize_strings(arr: list) -> list:
    """
    Возвращает список строк, начинающихся с заглавной буквы.

    :param arr: исходный список строк.
    :return: list
    """
    return list(map(lambda x: x.capitalize(), arr))


# Задача 3 (на рекурсию).
# Дано натуральное число N. Выведите слово YES, если число N является
# точной степенью двойки, или слово NO в противном случае.

# Для решения задачи, будем делить заданное число на 2,
# пока не получим результат равный 2 или остаток от деления у нас не будет равен 0.

def exact_degree_two(num):
    """
    Определяет, является ли заданное число точной степенью числа 2.

    :param num: заданное число.
    :return: string
    """
    result = num / 2
    while result % 2 == 0 and result >= 2:
        exact_degree_two(result)
        result /= 2
    return 'YES' if result == 2 or result == 1 else 'NO'


def main():
    # Задача 1
    # arr = list_of_integers(20)
    # print(f'Исходный список: {arr}')
    # print(f'Сумма нечётных чисел, не превосходящих 11: {sort_sum(arr)}')

    # Задача 2.
    # lst = ['dsfasdfsdf', 'rtrthrt', 'yuiyui', 'xczxc', 'dfgdfg']
    # print(capitalize_strings(lst))

    # Задача 3.
    number = int(input('Введите натуральное число: '))
    print(exact_degree_two(number))


if __name__ == '__main__':
    main()

