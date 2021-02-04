# Морозов Е.И. группа: Python 026

# Задача 1
"""
Увидев задачу, первое, что пришло мне на ум, это выводить результат
конкатенации двух строк.
Первая строка будет являться результатом дублирования строки symbol_one
на (multiplier_one) кол - во раз.
Вторая строка соотвественно: symbol_two на multiplier_two раз.
Формирование результирующей строки и её вывод организуем с помощью
цикла while.
В начале выполнение программы, спрашиваем у пользователя о высоте
пирамиды.
Также можно было реализовать отрисовку другими символами, спросив
об этом пользователя, но в рамках домашнего задания я этого не делал.
"""


def build_pyramid():
    height = int(input('Какой высоты пирамиду будем строить:'))
    multiplier_one = height - 1
    symbol_one = " "
    multiplier_two = 1
    symbol_two = "#"
    while multiplier_one >= 0:
        result_string = multiplier_one * symbol_one + multiplier_two * symbol_two
        print(result_string)
        multiplier_one -= 1
        multiplier_two += 1


"""
Так же, можно реализовать построение через цикл for.
"""


def build_pyramid_1(height):
    for i in range(height):
        print(' ' * (height - 1 - i) + '#' * (i + 1))


# Задача 2
"""
Увидев условие задачи, сразу же напрашивается применить для решения
алгоритм бинарного поиска.
"""


def guess_num():
    hidden_number = int(input('Загадайте число от 0 до 100 и введите его:'))
    low = 0
    high = 100
    while True:
        middle = (high + low) // 2
        if middle == hidden_number:
            print('Вы загадали:', middle)
            break
        else:
            question = 'Ваше число больше (у - да, n - нет) ' + str(middle) + '?'
            answer = input(question)
            if answer == 'y':
                low = middle + 1
            elif answer == 'n':
                high = middle - 1
            else:
                print('Ответ неверный, отвечайте y - да или n - нет.')


def main():
    build_pyramid()
    build_pyramid_1(10)
    guess_num()


if __name__ == '__main__':
    main()
