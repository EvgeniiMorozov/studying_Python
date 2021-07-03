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
import time
import threading


# Task-1


def generate_rand_nums(length: int) -> list:
    """Генерирует список со случайными числами от 1 до 1000 заданной длины length"""
    return [randint(1, 100) for _ in range(length)]


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


# Альтернативное решение

def create_file(event: threading.Event):
    event.set()
    with open('nums.txt', "w", encoding="utf-8") as f:
        for _ in range(100000):
            num = str(randint(1, 10000)) + "\n"
            f.write(num)
    event.clear()


def sum_nums(event):
    event.wait()
    sum = 0
    with open("nums.txt") as f:
        for line in f:
            sum += int(line.strip())
    return sum


def mean_nums(event):
    event.wait()
    sum = 0
    count = 0
    with open("nums.txt") as f:
        for line in f:
            sum += int(line.strip())
            count += 1
    return sum / count

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
    for x in range(2, ceil(num / 2)):
        return num % x != 0


# def list_wrapper(func, array: list) -> list:
#     """Декоратор, для передачи элементов списка на вход функции, принимающей число"""
#     def wrapper(func):
#         for num in array:
#             func(num)
#     return wrapper


def factorials_list(nums: list) -> list:
    """Получает на вход список с числами, отдает список с факториалами чисел"""
    return [fact(num) for num in nums]


def primes_list(nums: list) -> list:
    """Получает на вход список с числами, на выходе список с простыми числами"""
    return list(filter(lambda num: isprime(num) == True, nums))


def fill_file(file: str) -> None:
    """Заполняет файл строкой со случайными числами"""
    with open(file, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, generate_rand_nums(100))))


def read_file(file: str) -> list:
    """Считывает файл и возвращает список чисел"""
    with open(file, "r", encoding="utf-8") as f:
        result = f.read()
    return [int(el) for el in result.split()]


def multithread_work_2(file: str):
    """
    Решение 2 задачи ДЗ. Ждём от пользователя ввода имени файла, далее с помощью функции fill_file
    создаём файл с заданным названием и записываем туда строку с числами.
    Попутно реализуем функцию read_file, которая считывает информацию из файла и преобразует его в список с числами.
    Далее инициализируем многопоточный пул и выдаём на исполнение 2 задачи: на вычисление факториалов;
    на определение простых чисел из списка чисел.
    Результаты вычислений записываем в файл - result.txt.
    """
    fill_file(file)
    with cf.ThreadPoolExecutor(max_workers=None) as executor:
        future1 = executor.submit(primes_list, read_file(file))
        future2 = executor.submit(factorials_list, read_file(file))
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(f"Список простых чисел: {future1.result()}\n")
        f.write(f"Факториалы чисел: {future2.result()}\n")


def main():

    # Task-1
    # print(generate_rand_nums(30))
    # multithread_work()

    # Task-2
    # print(isprime(11))
    # print(fact(58))
    # filename = input("Введите имя файла: ")
    # multithread_work_2(filename)
    # create_file()

    start_time = time.time()
    # lock = threading.Lock()
    event = threading.Event()
    with cf.ThreadPoolExecutor() as executor:
        future1 = executor.submit(create_file)
        future2 = executor.submit(sum_nums)
        future3 = executor.submit(mean_nums)
    end_time = time.time()
    print(future2.result())
    print(future3.result())
    print(f"Время: {end_time - start_time}")

    print(f"Проверка суммы: {sum_nums(event)}")


if __name__ == "__main__":
    main()
