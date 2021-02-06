import math
import random

def check_word(word):
    # if word == 'мама':
    #     return 'да, это мама'
    # else:
    #     return 'нет, это не мама'
    return 'Да, это мама' if word == 'мама' else 'Нет, это не мама'


def get_greatest_num(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


def get_greatest_num2(arr):
    print(arr)
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(f'наибольшее число: {max}')


def f(x):
    if x > 0:
        return 2 * x - 10
    elif x == 0:
        return 0
    else:
        return 2 * abs(x) - 1

"""
Вводятся два целых числа. Проверить делится ли первое на второе.
Вывести на экран сообщение об этом,
а также остаток (если он есть) и частное (в любом случае).
"""


def check_div(a, b):
    mod = a % b
    if mod == 0:
        print(f'{a} делится на {b} и равно {a // b}')
    else:
        print(f'{a} не делится на {b} и получается {a // b}, а остаток {mod}')


"""
Найти сумму и произведение цифр, введенного натурального числа.
Например, если введено число 325, то сумма
его цифр равна 10 (3+2+5), а произведение 30 (3*2*5).
"""


def get_sum_and_mul(num):
    string = str(num)
    arr = list(string)
    sum = 0
    mul = 1
    for i in range(len(arr)):
        sum += int(arr[i])
        mul *= int(arr[i])
    print(f'Число {num}\nСумма цифр числа равна {sum}\nПроизведение цифр числа равно {mul}')


"""
Вывести на экран ряд натуральных чисел от минимума до максимума с шагом.
Например, если минимум 10, максимум 35, шаг 5, то вывод должен
быть таким: 10 15 20 25 30 35. Минимум, максимум и шаг
указываются пользователем (считываются с клавиатуры).
"""


def get_nums(min, max, step):
    min = int(min)
    max = int(max)
    step = int(step)
    for i in range(min, max+1, step):
        print(i, end=' ')
    print()


def fact(num):
    mul = 1
    for i in range(2, num+1):
        mul *= i
    print(f'Факториал {num} равен {mul}')


"""
Проверить корректность работы генератора псевдослучайных чисел
языка программирования с помощью оценки вероятности выпадения
четных чисел на выборке не меньше 1000 случайных чисел.
"""


def check_random_gen(arr):
    even = 0
    for num in arr:
        if num % 2 == 0:
            even += 1
    print(f'{arr}\nВ этой последовательности {even} чётных чисел.')


def main():
    # a = 1 + 2
    # print(check_word('мама'))
    # print(check_word('папа'))
    # a = 5
    # b = 8
    # c = 12
    # print(get_greatest_num(a, b, c))
    # arr = [
    #     [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #     [100],
    #     [-1, 10000, 2, 23, 6, 7],
    #     [9, 8, 7, 6]
    # ]
    # for list in arr:
    #     get_greatest_num2(list)
    # arr = [-1, 0, 1, 2, 3, 4, 5]
    # for num in arr:
    #     print(f'{num=}')
    #     print(f'Y = {f(num)}')
    # arr = [
    #     [4, 2],
    #     [6, 7],
    #     [1, 100],
    #     [100, 25],
    #     [26, 25]
    # ]
    # for l1 in arr:
    #     check_div(l1[0], l1[1])
    # arr = [13, 145, 42, 563]
    # for i in arr:
    #     get_sum_and_mul(i)
    # nums_str = input('Введите min, max, step с клавиатуры: ')
    # nums_arr = nums_str.split(' ')
    # get_nums(*nums_arr)
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # for num in arr:
    #     fact(num)
    # Task 8
    arr = []
    N = 1200
    for i in range(N):
        random_number = random.randint(1, 1000000)
        arr.append(random_number)
    check_random_gen(arr)
    # pass


if __name__ == '__main__':
    main()



