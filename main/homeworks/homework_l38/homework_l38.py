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
from math import ceil


# Task-1


def generate_rand_nums(length: int) -> list:
    """Генерирует список со случайными числами от 1 до 1000 заданной длины length"""
    return [randint(1, 1000) for _ in range(length)]


def multithread_work():
    """
    Решение 1го задания. С помощью контекстного менеджера инициализируется многопоточный пул с числом воркеров 3.
    Выдаем им 3 задачи:
    - С помощью ранее созданной функции generate_rand_nums формируем список и результат записываем в future1;
    - Воспользовавшись данными из future1 (future1.result()) считаем среднее арифметическое списка и сумму
      его членов и записываем их в переменные future2 и future3 соответственно.
    С помощью функции print организован вывод данных.
    """
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(generate_rand_nums, 30)
        future2 = executor.submit(lambda lst: sum(lst) / len(lst), future1.result())
        future3 = executor.submit(sum, future1.result())
    print(f"Сгенерированный список: {future1.result()}")
    print(f"Среднее арифметическое значение списка: {future2.result()}")
    print(f"Сумма всех членов списка: {future3.result()}")


# Task-2


def fact(num: int) -> int:
    """Вычисляет факториал заданного числа num"""
    if num == 1:
        return 1
    return num * fact(num - 1)


def isprime(num: int) -> bool:
    """Проверяет, является ли число, простым"""
    if num == 1:
        return False
    for x in range(2, ceil(num/2)):
        return num % x != 0


def main():

    # Task-1
    # print(generate_rand_nums(30))
    # multithread_work()

    # Task-2
    print(isprime(11))


if __name__ == "__main__":
    main()
