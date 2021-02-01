"""
Домашняя работа к уроку 2. Состоит из обязательного задания и необязательного.
Оценка выставляется только за обязательное задание, второе же только для интереса
и практики своих умений.

Задание 1 (обязательное):
Написать реализацию функции build_pyramid(), которая рисует (печатает) в консоли пирамидку:
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########
Для решения задачи это может помочь:

Функция print() (параметр end)
https://www.internet-technologies.ru/articles/funkcii-print-v-python.html

Строки (дублирование):
https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

------------------------------------------------------------------------------

Задание 2 (необязательное):
Дана фунция guess_num(), которая на вход принимает загаданное число num, и пытается
его удагать. В данный момент она реализована не так хорошо, как можно было бы.
Предлагается написать реализацию получше.
"""

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


# Задача 2
"""
Увидев условие задачи, сразу же напрашивается применить для решения
алгоритм бинарного поиска.
"""


# def guess_num(num):
#     """Игра в угадай число."""
#     start_num = 1
#     while True:
#         if start_num == num:
#             print('Ваше число это:', start_num)
#             break
#         question = 'Ваше число больше ' + str(start_num) + '?'
#         answer = input(question)  # либо y - да, либо n - нет
#         if answer == 'y':
#             start_num *= 2
#         elif answer == 'n':
#             start_num = start_num // 2 + 1  # start_num = start_num // 2
#         else:
#             print('Вы неправильно ввели ответ. Можно только y или n')
# upper_bound lower_bound


def guess_num():
    hidden_number = int(input('Загадайте число и введите его:'))
    # алгоритм определения участка поиска
    low = 1
    high = 100
    while True:
        middle = (high + low) // 2
        if middle == hidden_number:
            print('Загаданное число равно:', middle)
            break
        else:
            question = 'Ваше число больше (+) или меньше (-) ' + str(middle) + '?'
            answer = input(question)
            if answer == '+':
                low = middle + 1
            elif answer == '-':
                high = middle - 1
            else:
                print('Ответ неверный, отвечайте y - да или n - нет.')


def main():
    build_pyramid()
    guess_num()


if __name__ == '__main__':
    main()
