# Морозов Е.И. Группа: Python026

# Задача 1 (на файл). Дан текстовый файл, содержащий целые числа.
# Удалить из него все четные числа (файл создать самому).

# Задача 2 (на файлы). Получить файл g, состоящий из строк файла f, содержащих заданную строку S (файлы создать самому).

# Задача 3 (на множества и файлы). Есть два файла с разным большим текстом в каждом. Реализовать функцию, которая берёт
# каждый файл и выводит в консоль общие слова (которые есть и в первом и во втором файлах) (файлы создать самому).

from random import randint
import shutil


# Задача 1.
def delete_even_nums_in_file(file):
    # создаем копию исходного файла для сравнения
    shutil.copy(f'{file}', 'template.txt')

    # Считываем строки в список и разбиваем их на подписки
    def _read(file):
        f = open(f'{file}', 'r', encoding='UTF-8')
        lst = [line.strip('\t\n').split() for line in f.readlines()]
        f.close()
        # print(lst)
        return lst

    # Сортируем подсписки с помощью функции filter()
    def _sort(arrays):
        sort_arr = [' '.join(list(filter(lambda el: int(el) % 2 != 0, array))) for array in arrays]
        # print(sort_arr)
        return sort_arr

    # Записываем отсортированные данные в файл (по сути, мы создаем новый файл с таким же именем и туда заливаем данные)
    def _write(file, arrays):
        f = open(f'{file}', 'w', encoding='UTF-8')
        for arr in arrays:
            f.write(f'{arr}\n')
        f.close()

    return _write(file, _sort(_read(file)))


def get_string_of_rnd_nums(n):
    return ' '.join(str(el) for el in [randint(0, 100) for _ in range(n)])


def get_rnd_file(file_name, number_of_lines):
    file = open(f'{file_name}.txt', 'w')
    for num in range(number_of_lines):
        file.write(get_string_of_rnd_nums(randint(0, 10)) + '\n')
    file.close()


# Задача 3.



def main():
    get_rnd_file('example', 5)
    delete_even_nums_in_file('example.txt')


if __name__ == '__main__':
    main()
