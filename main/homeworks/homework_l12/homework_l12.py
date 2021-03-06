# Морозов Е.И. группа: Python026.

# Задача 1. Дан текстовый файл, состоящий из строк "Привет" и "Мир".
# Каждая строка файла содержит только одно из двух слов.
# Пример файла:
# Привет
# Привет
# Мир
# Привет
# Мир
# Мир
# Привет
# Написать функцию, которая пробегается по файлу и печатает то, что
# в текущей строке, но обязательно печает слова "Привет" и "Мир" по
# очереди.
# Пример вывода для файла выше:
# Привет
# Мир
# Привет
# Мир


# Задача 2. На вход подается строка, состоящая из круглых скобок.
# Выведите True, если скобки вложены правильно и False, если нет.
#
# Например, если входная строка (()(())), то ответ должен быть True.
# А если ()), то False.

from random import choice


# Задача 1.
# Вобщем, я не правильно понял условие задачи и написал 2 функции:
# 1. check_words() - читает файл построчно и там где встречаются повторяющиеся строки, между ними вставляются
#                   недостающая строка, чтоб не было повторений. Результат записывается в файл: result.txt;
# 2. check_words_1() - читает файл построчно и удаляет повторяющиеся строки.
#                       Результат записывается в файл: result_1.txt.

# Дополнительно, я написал функцию gen_sample_file(), которая формирует файл "sample.txt",
# состоящий из строк "Привет" и "Мир".
def check_words(filename):

    # В переменную state будем записывать предыдущую строку.
    state = ''
    with open(filename, 'r', encoding='UTF-8') as file1:
        with open('result.txt', 'w', encoding='UTF-8') as file2:
            # C помощью цикла поочередно считываем строки из файла.
            for line in file1:
                # Если state не совпадает с текущей строкой line, то записываем строку во второй файл.
                if line.strip('\n') != state:
                    file2.write(line)
                    state = line.strip('\n')
                # Если state совпадает с line, то определяем, чему равна переменная state:
                else:
                    if state == 'Привет':

                        # Первой строкой печатаем "Мир", а за ней текущую строку.
                        file2.write('Мир\n' + line)
                        # file2.write('*Мир\n' + line)  # для наглядности перед недостающей строкой вставил *

                        # Переменной state присвоим значение "Привет".
                        state = 'Привет'

                    else:

                        # Первой строкой печатаем "Мир", а за ней текущую строку.
                        file2.write('Привет\n' + line)
                        # file2.write('*Привет\n' + line)  # для наглядности перед недостающей строкой вставил *

                        # Переменной state присвоим значение "Мир".
                        state = 'Мир'


def check_words_1(filename):
    # В переменную state будем записывать предыдущую строку.
    state = ''
    with open(filename, 'r', encoding='UTF-8') as file1:
        with open('result_1.txt', 'w', encoding='UTF-8') as file2:

            # C помощью цикла поочередно считываем строки из файла.
            for line in file1:

                # Если state не совпадает с текущей строкой line, то записываем строку во второй файл.
                if line.strip('\n') != state:
                    file2.write(line)

                    # Переменной state присвоим значение текущей строки.
                    state = line.strip('\n')


# Работа над ошибками.
def get_lines(file: str) -> None:
    with open(file, 'r', encoding='UTF-8') as file:
        buffer = None
        for line in file:
            if buffer != line:
                print(line, end='')
                buffer = line


def gen_sample_file(n):
    """
    Создаёт файл "sample.txt" из n строк, состоящих из слов "Привет" или "Мир".

    :param n: количество строк
    :return: file
    """
    with open('sample.txt', 'w', encoding='UTF-8') as f:
        for _ in range(n):
            f.write(f'{choice(["Привет", "Мир"])}\n')


# Задача 2.
def check_parentheses(string: str) -> bool:
    return True if string.count('(') == string.count(')') else False


# Работа над ошибками.
def check_parentheses_1(string: str) -> bool:
    buffer = []
    for parenthes in string:
        if parenthes == '(':
            buffer.append(parenthes)
        elif parenthes == ')':
            if not buffer:  # аналог len(buffer) == 0
                return False
        buffer.remove('(')
    print(buffer)
    return True if not buffer else False


def main():
    # Задача 1.
    # gen_sample_file(20)
    # check_words('sample.txt')
    # check_words_1('sample.txt')
    # get_lines('sample.txt')

    # Задача 2.
    arr = [
        '(()(()))',
        '())',
        '(((()))))))',
        '))((',
        '()()('
    ]
    for line in arr:
        # print(check_parentheses(line))
        print(check_parentheses_1(line))


if __name__ == '__main__':
    main()
