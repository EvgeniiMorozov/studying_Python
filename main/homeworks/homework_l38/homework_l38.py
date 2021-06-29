"""
Задание 1. При старте приложения запускаются три потока. Первый поток заполняет
список случайными числами. Второй поток находит сумму элементов списка,
а третий поток среднеарифметическое значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран.

Задание 2. Пользователь с клавиатуры вводит путь к файлу. После чего запускаются
три потока. Первый поток заполняет файл случайными числами. Второй поток находит
все простые числа, а третий поток факториал каждого числа в файле. Результаты поиска
каждый поток должен записать в новый файл.

Подсказка: можно воспользоваться высокоуровневой библиотекой concurrent.futures для
создания пула потоков.

Нюансы реализации разрешаются программистом.
"""

import concurrent.futures as cf
from random import randint


# Task-1

def generate_rand_nums(length: int):
    """Генерирует список со случайными числами от 1 до 1000 заданной длины length"""
    return [randint(1, 1000) for _ in range(length)]


def multithread_work():
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(generate_rand_nums, 30)
        future2 = executor.submit(lambda lst: sum(lst)/len(lst), future1.result())
        future3 = executor.submit(sum, future1.result())
    print(f"Сгенерированный список: {future1.result()}")
    print(f"Среднее арифметическое значение списка: {future2.result()}")
    print(f"Сумма всех членов списка: {future3.result()}")


def main():

    # Task-1
    # print(generate_rand_nums(30))
    multithread_work()


if __name__ == '__main__':
    main()
