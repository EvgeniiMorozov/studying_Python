import random


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


# Task_3
# Проверить все ли символы в строке являются заглавными.
# Если строка пустая или в ней нет букв - функция должна вернуть True.
# Входные данные: Строка.
# Выходные данные: Логический тип.
# Условия: a-z, A-Z, 1-9 и пробелы
def is_all_upper(text: str) -> bool:
    # if text.isupper():
    #     return True
    # elif text == '':
    #     return True
    # elif len(text) == text.count(' '):
    #     return True
    # else:
    #     return False
    return True if text.isupper() or text == '' or len(text) == text.count(' ') else False


# Task_4
def square_digits(num):
    lst = [int(i)**2 for i in str(num)]
    res = ''
    for el in lst:
        res += str(el)
    return res


# Task_5
def accum(string):
    return '-'.join((el*(i+1)).capitalize() for i, el in enumerate(string.lower()))


# Task_6
def to_camel_case(text: str):
    camel_text = ''
    if text.count('-') > 0:
        lst = text.split('-_')
        if lst[0][0].isupper():
            camel_text = ''.join((string.capitalize() for string in lst))
        else:
            camel_text = lst[0].lower() + ''.join((lst[i].capitalize() for i in range(1, len(lst))))

    if text.count('_') > 0:
        lst = text.split('_')
        if lst[0][0].isupper():
            camel_text = ''.join((string.capitalize() for string in lst))
        else:
            camel_text = lst[0].lower() + ''.join((lst[i].capitalize() for i in range(1, len(lst))))

    return camel_text


# Task_7
def sum_numbers(text: str) -> int:
    # your code here
    accumulator = 0
    for el in text.split():
        if el.isdigit():
            accumulator += int(el)
    return accumulator


# Task_8
# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
# Для пустого массива результат всегда 0 (ноль).
# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int).
# Предусловия: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)
def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    return 0 if len(array) == 0 else sum(array[::2]) * array[-1]


# Task_9
# Давайте научим наших роботов отличать слова от чисел.
# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.
# Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100
def checkio_1(words: str) -> bool:
    counter = 0
    for arr in words.split():
        if counter == 3:
            break
        else:
            if arr.isalpha():
                counter += 1
            else:
                counter = 0
    return True if counter >= 3 else False


# Task_10
# Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
# даже если это часть другого слова. Все строки даны в нижнем регистре.
# Входные данные: Последовательность строк.
# Выходные данные: Текст, как строка.
# Предусловие:
# 0 < len(phrases) < 42
def left_join(phrases: tuple) -> str:
    return ','.join(phrase for phrase in phrases).replace('right', 'left')


def main():
    # Task_1
    # lst = random_turns(23)
    # counting_rotates(lst)

    # Task_2
    # print(end_zeros(1200))
    # print(end_zeros_1(1200))

    # Task_3

    # Task_4
    # square_digits(456)

    # Task_5
    # accum('Brrt')

    # Task_6
    # strings = ["the-stealth-warrior", "The_Stealth_Warrior"]
    # for string in strings:
    #     print(to_camel_case(string))

    # Task_7
    # arrays = [
    #     [0, 1, 2, 3, 4, 5],
    #     [1, 3, 5],
    #     [6],
    #     []
    # ]
    # for arr in arrays:
    #     print(checkio(arr))

    # Task_9
    # array = [
    #     "Hello World hello",
    #     "He is 123 man",
    #     "1 2 3 4",
    #     "bla bla bla bla",
    #     "Hi",
    #     "sdadsf dsfsdfs sdfdsf 1 sdfsdf"
    # ]
    # for words in array:
    #     print(f'{words}: {checkio_1(words)}')

    # Task_10
    phrases = (
        ("left", "right", "left", "stop"),
        ("bright aright", "ok"),
        ("brightness wright",),
        ("enough", "jokes")
    )
    for phrase in phrases:
        print(left_join(phrase))


if __name__ == '__main__':
    main()
