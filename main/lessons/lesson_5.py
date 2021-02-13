from functools import reduce


def get_pos_maxlen_strings(a, b, c):
    print(a, b, c)


def print_score(score_str):
    print(score_str)


def inc_num(n):
    return n + 1


def kms_to_ms(num):
    return num / 3.6


def main():
    # Функции и методы
    # get_pos_maxlen_strings(1, 2, 3)
    # string = 'пример'
    # print(get_pos_maxlen_strings.__name__)

    # Лямбда-функции
    # func = lambda x: x.upper()
    # print(func('example'))
    # func1 = lambda x: x if x > 0 else None
    # print(func1(-1))
    # score = 100
    # for i in range(5):
    #     print_score(lambda i: f'Ваши очки: {i + score}')
    # arr = [1, 2, 3, 4, 5]
    # for i, elem in enumerate(arr):
    #     print(lambda i, elem: i+elem)

    # Функция map()
    # arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # arr_2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # print(f'{arr=}')
    # print(f'{arr_2=}')
    # Первый вариант инкрементирования элементов списка
    # for i in range(len(arr)):
    #     arr[i] += 1
    # print(arr)
    # Второй вариант
    # inc_arr = list(map(inc_num, arr))
    # print(inc_arr)
    # Третий вариант
    # inc_arr = list(map(lambda x: x+1, arr))
    # print(inc_arr)

    # filter()
    # result = list(filter(lambda x: x > 5, arr))
    # print(result)
    # recipe = ['тесто', 'томатная паста', 'сыр', 'салями', 'салями']
    # result = list(filter(lambda x: x == 'салями', recipe))
    # print(result)

    # Функция reduce()
    # сумма всех чисел последовательности
    # result = reduce(lambda x, y: x+y, arr)
    # print(result)

    # поиск максимального числа
    # result = reduce(lambda x, y: x if x > y else y, arr)
    # print(result)

    # сложения двух чисел из разных списков
    # result = list(map(lambda x, y: x+y, arr, arr_2))
    # print(result)

    # сумма всех чисел из двух списков
    # result_map = list(map(lambda x, y: x+y, arr, arr_2))
    # print(f'{result_map=}')
    # result_reduce = reduce(lambda x, y: x+y, result_map)
    # print(f'{result_reduce=}')

    # result = reduce(lambda x, y: x+y, arr, 2)
    # print(result)

    # функция zip()

    # arr_1 = [1, 2, 3, 4, 5]
    # arr_2 = [6, 7, 8, 9, 0]
    # result_map = list(zip(arr_1, arr_2))
    # print(result_map)
    # print(dict(result_map))

    # arr = [18, 36, 72, 144]
    # result = list(map(kms_to_ms, arr))
    # print(result)

    # вернуть только чётные числа
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # result = list(filter(lambda x: x % 2 == 0, arr))
    # print(result)

    arr = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
    result = reduce(lambda x, y: x+y, list(filter(lambda x: x > 0, arr)))
    print(result)


if __name__ == '__main__':
    main()

