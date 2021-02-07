# По длинам трех отрезков, введенных пользователем, определить возможность существования
# треугольника, составленного из этих отрезков. Если такой треугольник существует, то
# определить, является ли он разносторонним, равнобедренным или равносторонним.
def is_triangle(side1, side2, side3):
    pass


# Переставить элементы заданного массива в обратном порядке, то есть произвести реверс массива.
# Способ 1. С помощью метода list.reverse().
def reverse_arr(arr):
    return arr.reverse()


# Способ 2. С помощью среза списка (требуется взять шаг среза -1).
def reverse_arr_1(arr):
    return arr[::-1]


# Способ 3. С помощью цикла for.
def reverse_arr_2(arr):
    new_arr = []
    for i in range(0, len(arr), -1):
        new_arr.append(arr[i])
    return new_arr


# Вводятся строки. Определить самую длинную строку и вывести ее номер на
# экран. Если самых длинных строк несколько, то вывести номера всех таких строк.
def get_pos_maxlen_strings():
    pass


def main():
    # Задача 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(arr.reverse())
    # print(arr[::-1])
    # print(reverse_arr(arr))
    # print(reverse_arr_1(arr))
    # print(reverse_arr_2(arr))
    # pass


if __name__ == '__main__':
    main()
