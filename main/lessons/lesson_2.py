import example

# function

# def smth():
#     pass  # ключевое слово (пропустить)
#
# def foo():
#     print('I`m function')
#     a = 6
#     b = 8
#     print('Rsult:', a + b)
#
# foo()

# Arguments
# def add_nums(a, b):
#     c = a + b
#     print(c)
#
#
# add_nums(12, 15)
# result = add_nums(12, 15)  # None
# print(result)

def add_nums(a, b):
    # a и b позиционные аргументы
    c = a + b
    return c


def guess_num(num):
    start_num = 10
    result = None
    while True:  # бесконечный цикл, но его можно прервать
        if start_num == num:
            print('Ваше число:', start_num)
            break
        question = 'Ваше число больше ' + str(start_num) + '?'
        answer = input(question)  # y - yes or n - no
        if answer == 'y':
            start_num *= 2
        elif answer == 'n':
            start_num = start_num // 2 + 1  # деление нацело
        else:
            print('Вы не правильно ввели ответ, можно y или n')


def main():
    # result = add_nums(12, 15)
    # print('Result:', result)
    #
    # result_1 = add_nums(b=14, a=21)
    # print('Result_1:', result_1)

    # imports
    # result_2 = example.mul_nums(70, 3)
    # print('Result_2:', result_2)

    # for i in range(4, 13, 2):
    #     print("Номер иттерации:", i)

    # for i in range(10):
    #     if i % 3 == 0:
    #         print('Делится на 3:', i)
    #     elif i % 3 == 1:
    #         print('Почти делится на 3:', i)
    #     else:
    #         print('Другой остаток', i)

    # num = 100
    # while num != 0:
    #     print('num =', num)
    #     num -= 10
    guess_num(50)




if __name__ == '__main__':
    main()
