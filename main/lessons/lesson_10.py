# Сортировки, хеш-таблицы, работа с файлами.

from random import randint, shuffle
import hashlib
import time

# Сортировка вставками.
def insertion_sort(arr):
    counter = 0
    for i in range(len(arr)):
        j = i - 1  # позиция элемента, стоящего слева от текущего
        key = arr[i]  # текущий элемент
        while arr[j] > key and j >= 0:
            counter += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(f'insertion_sort - общее кол-во операций на список {arr} из {len(arr)} элементов: {counter}')
    return arr


# Сортировка Шелла ().
def shel_sort(arr):
    d = len(arr) // 2
    counter = 0
    while d:
        for i, el in enumerate(arr):
            counter += 1
            while i >= d and arr[i-d] > el:
                counter += 1
                arr[i] = arr[i-d]
                i -= d
            arr[i] = el
        d = 1 if d == 2 else int(d * 5 / 11)
    print(f'Shell_sort - общее кол-во операций на список {arr} из {len(arr)} элементов: {counter}')
    return arr


# Хеш-таблицы.
# алгоритмы хэширования: md4, md5, sha1, sha2, sha3


def main():
    # сортировки Шелла и вставками
    # arr = [5, 4, 2, 7, 6, 3, 8, 1]
    # print(insertion_sort(arr))  # insertion_sort - общее кол-во операций на список [1, 2, 3, 4, 5, 6, 7, 8] из 8 элементов: 15
    # arr_1 = [5, 4, 2, 7, 6, 3, 8, 1]
    # print(shel_sort(arr_1))  # Shell_sort - общее кол-во операций на список [1, 2, 3, 4, 5, 6, 7, 8] из 8 элементов: 33
    # lst = []
    # N = 100
    # for _ in

    # Хеш
    # string = 'мама мыла раму'
    # string1 = 'мoма мыла раму'
    # hash_object = hashlib.md5(string.encode())
    # hash_object1 = hashlib.md5(string1.encode())
    # print(hash_object.hexdigest())  # fd8b2ae4a0c5bfe65b3d38b664b28667
    # print(hash_object1.hexdigest())  # d572f6f1ac05f05423144b343ac1b0ef

    # dct = {
    #     'one': 1,
    #     'two': 2,
    #     'three': 3
    # }

    # lst = [i for i in range(1000000)]
    # dct = {i: i for i in range(1000000)}
    # find_el = 89737
    # start_time = time.time()
    # print(lst.index(find_el))
    # print(f'поиск в списке занял {time.time() - start_time:.2}')
    # start_time = time.time()
    # print(dct.get(find_el))
    # print(f'поиск в словаре занял {time.time() - start_time:.2}')

    # Работа с файлами
    # f = open('1.txt', 'a')
    # f.write('New line 2')
    # # print(data)
    # f.close()

    # f = open('1.txt', 'r')
    # print(*f)
    # f.close()

    # f = open('1.txt', 'r')
    # data = f.read(3)
    # print(data)
    # f.close()

    # f = open('1.txt', 'r')
    # data = f.readline()
    # print(data)
    # f.close()

    # запись в файл с автоматической новой строкой
    # f = open('1.txt', 'w')
    # print('data 1', file=f)
    # print('data 2', file=f)
    # f.close()

    # вносим русские буквы
    f = open('3.txt', 'wb')
    string = '\nНовая строка'.encode()
    f.write(bytes(string))
    f.close()


if __name__ == '__main__':
    main()

