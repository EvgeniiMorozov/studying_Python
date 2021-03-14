# Модуль Collections.
import collections
import string


def main():
    # type Counter.

    strings = 'мама мыла раму'
    letters = string.ascii_letters
    list_counts = collections.Counter(strings)
    # По сути, это обычный словарь
    print(list_counts)
    # получение всех элементов
    print(list(list_counts.elements()))
    # Наиболее встречающиеся элементы
    print(list_counts.most_common(2))


if __name__ == '__main__':
    main()
