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
def check_words(filename):
    with open(filename, 'r', encoding='UTF-8') as file1:
        with open('result.txt', 'w', encoding='UTF-8') as file2:
            counter_hello = 0
            counter_world = 0
            for line in file1:
                if line.strip('\n') == 'Привет':
                    file2.write(line + f'{"Мир"}\n')
                    counter_hello += 1
                if line.strip('\n') == 'Мир':
                    file2.write(f'{"Привет"}\n' + line)
                    counter_world += 1
    print(f'Слово "Мир" упоминается\t{counter_world} раз.\nСлово "Привет" упоминается\t{counter_hello} раз.')


def gen_sample_file(num):
    with open('sample.txt', 'w', encoding='UTF-8') as f:
        for _ in range(num):
            f.write(f'{choice(["Привет", "Мир"])}\n')


# Задача 2.
def check_parentheses(string: str) -> bool:
    return True if string.count('(') == string.count(')') else False


def main():
    # Задача 1.
    # gen_sample_file(20)
    check_words('sample.txt')

    # Задача 2.
    # arr = [
    #     '(()(()))',
    #     '())'
    # ]
    # for line in arr:
    #     print(check_parentheses(line))


if __name__ == '__main__':
    main()
