from functools import reduce


# Task_1
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
def task_1():
    res = reduce(lambda x, y: x + y, list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1000)])))
    filtered_list = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, [i for i in range(1000)]))
    print(f'{filtered_list=}')
    return res


# Task_2
# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
def even_sum_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):

        if b % 2 == 0:
            yield b

        a, b = b, a + b


def main():
    # print(task_1())
    print(sum(even_sum_fibonacci(4000000)))


if __name__ == '__main__':
    main()
