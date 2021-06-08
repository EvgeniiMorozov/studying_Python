"""
Создайте приложение для работы в библиотеке. Оно должно оперировать
следующими сущностями: Книга, Библиотекарь, Читатель.

Книга представляет собой произвольный набор данных (напр. автор, название).

Билиотекарь умеет добавлять, удалять и изменять Книги. У него находятся все Книги.

Читатель умеет читать книги. Для этого ему нужно взять какую-либо Книгу у Библиотекаря.

При реализации используйте любой из структурных паттернов проектирования.
Структура и реализация остаётся за программистом.
"""
from random import choice


BOOK_GENRES = ['Фэнтэзи', 'Научная фантастика', 'Приключения', 'Драма', 'Детектив', 'Поэзия']
BOOK_AUTHORS = [
    'Иван Иванов',
    'Андрей Андреев',
    'Василий Васильев',
    'Дмитрий Дмитриев',
    'Григорий Григорьев',
    'Михаил Михайлов'
]
BOOK_NAMES = [
    'Природа смешариков.',
    'Шварц против Сталлоне.',
    'Восстание телепузиков.',
    'Смешарики наносит ответный удар.',
    'Старая надежда.',
    'В поисках Джеки Чана.',
    'Атака телепузиков.',
    'Мистер Андерсон.'
]


class Book:
    def __init__(self):
        self.author: str = str()
        self.genre: str = str()
        self.name: str = str()

    def __str__(self):
        info = f'Эта книга называется: {self.name},\n' \
               f'\tнаписал её выдающийся автор: {self.author},\n' \
               f'\t непревзойдённый мастер жанра {self.genre}.'
        return info


class Reader:
    def __init__(self, name):
        self.__name = name

    def choose_book(self, genre):
        print(f'Читатель {self.__name} хочет почитать что-нибудь из {genre}.')

    def read_book(self, book):
        print(f'Читатель {self.__name} читает книгу {book}.')

    def get_name(self):
        return self.__name


class Librarian:
    def add_book(self):
        pass

    def change_book(self):
        pass

    def delete_book(self):
        pass

    def __create_book(self):
        pass


class LibraryFacade:
    pass


def main():
    pass


if __name__ == '__main__':
    main()




