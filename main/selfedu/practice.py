import random
import collections
from functools import reduce


# Task_1

# Дан список, состоящий из произвольного числа направлений
# поворотов («left» и/или «right»). Напишите функцию, которая
# будет принимать этот список и определять, сколько полных оборотов сделано.

# Сделаем допущение, что для полного оборота надо совершить 4 поворота в одну сторону.

def random_turns(n):
    """
    Функция-генератор списка случайных перемещений "left" и "right".

    :param n: количество перемещений.
    :return: список перемещений.
    """
    lst = []
    for i in range(n):
        lst.append('left') if random.randint(0, 1) == 0 else lst.append('right')
    return lst


def counting_rotates(lst):
    count_left = 0
    count_right = 0
    for turn in lst:
        # count_left += 1 if turn == 'left' else count_right += 1
        if turn == 'left':
            count_left += 1
        else:
            count_right += 1
    print(f'Список направлений: {lst}')
    print(f'{count_left=}\t\t{count_right=}')
    print(f'Полных оборотов влево: {count_left // 4}\nПолных оборотов вправо: {count_right // 4}')


# Task 2

# Попробуйте выяснить какое количество нулей содержит данное число в конце.
# Входные данные: Положительное целое число (int).
# Выходные данные: Целое число (int).
def end_zeros(num: int) -> int:
    count_zero = 0
    lst = list(str(num))
    lst.reverse()
    for i in lst:
        if int(i) == 0:
            count_zero += 1
        else:
            break
    return count_zero


def end_zeros_1(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))


"""
def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))

def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())

def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])

def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0

def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result

def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')

def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))
"""


def main():
    # Task_1
    # lst = random_turns(23)
    # counting_rotates(lst)
    # print(end_zeros(1200))
    print(end_zeros_1(1200))


if __name__ == '__main__':
    main()
