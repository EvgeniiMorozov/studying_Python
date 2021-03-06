# Сортировки, os.path, patlib.
import os.path
import os
from pathlib import Path

# Пирамидальная сортировка / Сортировка кучей / HeapSort
def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n, -1, -1):  # N
        heapify(arr, n, i)

    # извлекаем элементы из кучи один за другим и вставляем на свои места в списке
    for i in range(n-1, 0, -1):  # N-1
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i  # корень кучи
    l = 2 * i + 1  # левый потомок корня
    r = 2 * i + 2  # правый потомок корня

    # сущевует ли левый потомок, больший корня
    if l < n and arr[i] < arr[l]:
        largest = l
    # сущевует ли правый потомок, больший корня
    if r < n and arr[largest] < arr[r]:
        largest = r

    # меняем местами корень и последний элемент кучи
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def main():
    # f = open('demo.txt')
    # line = f.readline()
    # while line is not None:
    #     print(line)
    #     line = f.readline()
    # f.close()
    # try:
    #     with open('qwe.txt') as f:
    #         data = f.read()
    #     # num = 1 / 0
    # except FileNotFoundError as e:
    #     print(f'Файла {e.filename} не существует!', e.strerror)
    # except ZeroDivisionError as e:
    #     print(f'На ноль делить нельзя! {e.args}')
    # except:
    #     print(f'Непредвиденная ошибка!')
    # else:
    #     print('Отработаю только тогда, когда всё прошло без ошибок')
    # finally:
    #     print('Отработаю всегда, независимо от наличия исключений')

    # HeapSort

    # arr = [4, 2, 1, 3, 8, 0, 5, 9, 6, 7]
    # print(arr)
    # heap_sort(arr)
    # print(arr)

    # питоновский указатель на исполняемый файл
    # print(__file__)
    # путь к рабочей директории исполняемого файла
    # BASE_DIR = os.path.dirname(__file__)
    # print(BASE_DIR)

    # кортеж с конкретным файлом (директорией) и путем к нему
    # BASE_DIR = os.path.split(__file__)
    # print(BASE_DIR)

    # нормализованный абсолютный путь
    # BASE_DIR = os.path.abspath(__file__)
    # print(BASE_DIR)

    # базовое имя (файл или директория)
    # BASE_DIR = os.path.basename(__file__)
    # print(BASE_DIR)

    # составление путей
    # new_path = '/user/documents'
    # new_path2 = os.path.join('3.txt', new_path)
    # print(new_path2)

    # print(os.getcwd())  # путь к рабочей директории
    # os.mkdir('temp')
    # os.rmdir('temp')
    # os.mkdir('temp')
    # os.rename('temp', 'temp2')

    # current_dir = Path.cwd() / 'dir'
    # print(current_dir)

    # home_dir = Path.home()
    # print(home_dir)

    # path1 = os.path.join(os.getcwd(), '101')
    # path2 = os.path.join(path1, '101.txt')
    # print(path2)

    current_dir = Path.cwd()
    # print(current_dir)

    # if os.path.isdir(path1):
    #     print('Это путь к папке')

    # if current_dir.is_dir():
    #     current_dir.rmdir()
    # print(current_dir)

    print(list(current_dir.glob('**/*')))


if __name__ == '__main__':
    main()


