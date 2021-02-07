import random


# Task_1
# Заполнить один массив случайными числами, другой - введенными с клавиатуры числами,
# в ячейки третьего записать суммы соответствующих ячеек первых двух.
# Вывести содержимое массивов на экран.
def gen_arrays(arr):
    random_arr = []
    sum_arr = []
    # Решение 1
    # for i in range(len(arr)):
    #     random_arr.append(random.randint(0, 100))
    # for i in range(len(arr)):
    #     sum = int(arr[i]) + random_arr[i]
    #     sum_arr.append(sum)
    # Решение 2
    for i in range(len(arr)):
        random_arr.append(random.randint(0, 100))
        sum = int(arr[i]) + random_arr[i]
        sum_arr.append(sum)
    print(f'Пользовательский список {arr}')
    print(f'Список со случайными числами {random_arr}')
    print(f'Список с суммами элементов первых двух списков {sum_arr}')


# Task_2
# Заполнить массив вещественных чисел вводом с клавиатуры.
# Посчитать сумму и произведение элементов массива.
# Вывести на экран сам массив, полученные сумму и произведение его элементов.
def sum_elements(arr):
    sum = 0
    mul = 1
    for num in arr:
        sum += num
        mul *= num
    print(f'Сумма: {sum}\nПроизведение: {mul}')

# Task_3
# Сгенерировать 20 случайных целых чисел в диапазоне от -5 до 4, записать их в ячейки массива.
# Посчитать сколько среди них положительных, отрицательных и нулевых значений.
# Вывести на экран элементы массива и посчитанные количества.
def count(arr):
    zero = 0
    pos = 0
    neg = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i > 0:
            pos += 1
        else:
            neg += 1
    print(arr)
    print(f'Положительных чисел: {pos}\tОтрицательных {neg}\tНулей: {zero}')


# Task_3
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.
def counts():
    dict_counts = dict()
    for nat_num in range(2, 100):
        for div_num in range(2, 10):
            if nat_num % div_num == 0:
                dict_counts[str(div_num)] += 1
    print(dict_counts)


def main():
    # Task_1
    # user_data = input('Введите числа для списка через пробел: ')
    # arr = user_data.split(' ')
    # gen_arrays(arr)

    # Task_2
    # arr = [1, 2, 3, 4, 5, 6, 7, 8]
    # sum_elements(arr)

    # Task_3
    # arr = []
    # for _ in range(20):
    #     arr.append(random.randint(-5, 4))
    # count(arr)

    # Task_4
    # counts()
    pass


if __name__ == '__main__':
    main()
