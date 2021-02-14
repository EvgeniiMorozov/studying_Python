import sys
import string
from random import shuffle
from random import choice
from functools import reduce


# Аннотирование функций.
def func(key: int, key2: int) -> int:
    return key+key2


# sys.setrecursionlimit(2000)


# Рекурсия.
def rec_func(num):
    # if num <= 500:  # базовый случай выхода из рекурсии
    #     return num
    print(num)
    rec_func(num-1)


def fact(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result


def rec_fact(num):
    if num == 1:
        return 1
    return num * rec_func(num-1)


def gen_password(len_pass):
    alphabet = list(string.ascii_letters + string.digits + string.punctuation)
    shuffle(alphabet)
    password = ''
    for _ in range(len_pass):
        password += choice(alphabet)
    return password


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def sum_greater_and_lower(arr):
    # Решение с помощью цикла
    # min = arr[0]
    # max = arr[0]
    # for num in arr:
    #     if num < min:
    #         min = num
    #     elif num > max:
    #         max = num
    # print(f'{min=} | {max=} | Sum: {min+max}')

    # Решение с помощью функции высшего порядка
    min = reduce(lambda x, y: x if x < y else y, arr)
    max = reduce(lambda x, y: x if x > y else y, arr)
    print(f'{min=} | {max=} | Sum: {min + max}')

# вернуть минимальное чётное число из списка
def min_even(arr):
    even_lst = list(filter(lambda x: x % 2 == 0, arr))
    even_min = reduce(lambda x, y: x if x < y else y, even_lst)
    return even_min


# Дан массив.
def min_neib_els_sum(arr):
    min_sum = arr[0] + arr[1]
    pos = [0, 1]
    for i in range(len(arr)-1):
        if arr[i] + arr[i+1] < min_sum:
            min_sum = arr[i] + arr[i+1]
            pos = [i, i+1]
    print(f'{min_sum=} | {pos=}')


def get_num(num):
    # mul_k = 1
    # delimetr = 10
    # for k in range(10**7):
    #     bitness = 0
    #     copy_k= k
    #     while copy_k > 0:
    #         copy_k //= 10**bitness
    #         bitness += 1
    #     while k > 0:
    #         mul_k += k //


def get_num_1(num):
    pass


def main():
    # Unpackage
    # arr = ['123', '456']
    # # print(arr[0], arr[1])
    # print(func(*arr))  # распаковка

    # dct = {
    #     'key': 'mother',
    #     'key2': ' wash'
    # }
    # print(func(**dct))  # key='mother', key2='wash'
    # rec_func(1000)
    # print(f'Факториал: {fact(5)}')

    # Константы модуля string
    # ascii_lower = string.ascii_lowercase
    # print(ascii_lower)  # abcdefghijklmnopqrstuvwxyz
    # print(gen_password(10))

    # Сортировка пузырьком
    # arr = [5, 4, 6, 0, 1, 9, 2, 8, 7]
    # print(f'No sorting: {arr}')
    # print(f'Sort: {bubble_sort(arr)}')

    # Задачи
    # T-1
    arr = [1, 2, 3, 4, 5, 10]
    # sum_greater_and_lower(arr)
    print(min_even(arr))
    arr_1 = [9, 5, 6, 7, 8, 1, 9, 0, 9, 10]
    min_neib_els_sum(arr_1)


if __name__ == '__main__':
    main()
