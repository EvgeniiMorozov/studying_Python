# Морозов Е.И. Группа: Python026

# Задача 1 (на файл). Дан текстовый файл, содержащий целые числа.
# Удалить из него все четные числа (файл создать самому).

# Задача 2 (на файлы). Получить файл g, состоящий из строк файла f, содержащих заданную строку S (файлы создать самому).

# Задача 3 (на множества и файлы). Есть два файла с разным большим текстом в каждом. Реализовать функцию, которая берёт
# каждый файл и выводит в консоль общие слова (которые есть и в первом и во втором файлах) (файлы создать самому).

from functools import reduce
from random import randint
from re import IGNORECASE
from re import findall
import shutil


# Задача 1.
# Для проверки этой задачи, я сделал генератор файла со строками чисел get_rnd_file.
def delete_even_nums_in_file(file):
    # создаем копию исходного файла-template.txt для сравнения
    shutil.copy(f'{file}', 'template.txt')

    # Считываем строки в список и разбиваем их на подписки.
    def _read(file):
        f = open(f'{file}', 'r', encoding='UTF-8')
        lines = []
        for line in f.readlines():
            lines.append(findall(r'\d+', line))
        f.close()
        return lines

    # Сортируем подсписки с помощью функции filter().
    def _sort(arrays):
        sort_arr = [' '.join(list(filter(lambda el: int(el) % 2 != 0, array))) for array in arrays]
        return sort_arr

    # Записываем отсортированные данные в файл.
    # (но по сути, мы создаем новый файл с таким же именем и туда заливаем данные)
    def _write(file, arrays):
        f = open(f'{file}', 'w', encoding='UTF-8')
        for arr in arrays:
            f.write(f'{arr}\n')
        f.close()

    return _write(file, _sort(_read(file)))


# Генератор файла со случайными числами.
def get_rnd_file(file_name, number_of_lines):
    """
    Создаёт файл с заданными количеством строк, состоящих из случайных чисел.

    :param file_name: имя создаваемого файла
    :param number_of_lines: количество строк
    :return: file
    """

    def _get_string_of_rnd_nums(n):
        """Генерирует строку из n случайных чисел."""
        return ' '.join(str(el) for el in [randint(0, 100) for _ in range(n)])

    file = open(f'{file_name}', 'w')
    for num in range(number_of_lines):
        file.write(_get_string_of_rnd_nums(randint(0, 20)) + '\n')
    file.close()


# Задача 2.
# В этой задаче, для поиска заданной строки воспользуюсь методом findall() из модуля re.
def search_string(file, target_string):

    # Считываем информацию из файла построчно и возвращаем список.
    def _read(file):
        f = open(f'{file}', 'r', encoding='UTF-8')
        # для формирования списка воспользуемся генератором списка, попутно удалив из строк перенос строки (\n)
        lines = [line.strip('\n') for line in f.readlines()]

        return lines

    # Ищем совпадение заданной строки в строках файла.
    def _search_and_sort(array, string):
        new_array = []
        # с помощью цикла for пройдемся по всем строкам файла, ища совпадения с заданной строкой
        for arr in array:
            # условие совпадения - если у нас в строке есть совпадение с заданной строкой, то метод findall возвратит
            # нам НЕ пустую строку, эти строку, мы помещаем в список
            if len(findall(string, arr)) != 0:
                new_array.append(arr)

        return new_array

    # Записываем получивщийся список со строками в новый файл.
    def _write_file(lst):
        f = open('task2_result.txt', 'w', encoding='UTF-8')
        for line in lst:
            f.write(line + '\n')
        f.close()

    return _write_file(_search_and_sort(_read(file), target_string))


# Задача 3.
# Эту задачу я решил двумя способами, второй способ отличается от первого тем, что для извлечения слов из текста
# я пользуюсь регулярным выражением, из-за этого код получился более читаемым, чем в первом способе, и как мне кажется,
# более понятным для другого человека.

# Первый способ (для извлечения слов из текста, пользуюсь методами работы со строками)
def find_intersections(file_1, file_2):

    # Считываем файл в список.
    def _read_file(file):
        f = open(f'{file}', 'r', encoding='UTF-8')
        lst = [line.strip().split() for line in f.readlines()]
        f.close()
        return lst

    # Сортируем полученный список и преобразуем в множество.
    def _receive_set(lst):
        array = list(filter(lambda el: len(el.strip('-.,\'\"')) > 0, reduce(lambda arr, el: arr + el, lst)))
        new_arr = list(map(lambda el: el.strip('-.,\'\"'), array))
        return {el for el in new_arr}

    return _receive_set(_read_file(file_1)) & _receive_set(_read_file(file_2))


# Второй способ (для извлечения слов, воспользуюсь регулярным выражением)
def find_intersections_1(file_1, file_2):

    def _receive_set_from_file(file):
        f = open(f'{file}', 'r', encoding='UTF-8')
        lines = f.readlines()
        f.close()
        new_lst = []
        for line in lines:
            new_lst.append(findall(r'[A-ZА-ЯЁ]+', line, flags=IGNORECASE))
        return set(reduce(lambda arr, el: arr + el, new_lst))

    return _receive_set_from_file(file_1) & _receive_set_from_file(file_2)


def get_count_word_stat(filename1, filename2):
    with open(filename1, encoding='UTF-8') as f:
        data1 = f.read().split()
    with open(filename2, encoding='UTF-8') as f:
        data2 = f.read().split()
    # print(data1)
    # print(data2)
    repeated_words = set(data1) & set(data2)
    result = {word: (data1.count(word), data2.count(word)) for word in repeated_words}
    print(result)


def main():
    # Задача 1.
    # get_rnd_file('example.txt', 10)
    # delete_even_nums_in_file('example.txt')

    # Задача 2.
    # search_string('task2.txt', 'Моррель')

    # Задача 3.
    # print(find_intersections('task3_text1.txt', 'task3_text2.txt'))
    # print(find_intersections_1('task3_text1.txt', 'task3_text2.txt'))

    get_count_word_stat('task3_text1.txt', 'task3_text2.txt')


if __name__ == '__main__':
    main()
