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
               f'написал её выдающийся автор: {self.author},\n' \
               f'непревзойдённый мастер жанра {self.genre}.'
        return info


class Reader:
    def __init__(self, name):
        self.__name: str = name

    def choose_book(self, genre):
        print(f'Читатель {self.__name} хочет почитать что-нибудь из {genre}.')

    def read_book(self, book):
        print(f'Читатель {self.__name} читает книгу {book}.')

    def get_name(self):
        return self.__name


class Librarian:
    def __init__(self):
        self.book = None

    def add_book(self, genre):
        self.book = Book()
        self.book.genre = genre
        self.book.author = choice(BOOK_AUTHORS)
        self.book.name = choice(BOOK_NAMES)
        return self.book

    def change_book(self):
        pass

    def delete_book(self, book):
        print('Библиотекарь забрал книгу у читателя.')
        return book.kill()


class LibraryFacade:
    def __init__(self):
        self.librarian = Librarian()
        self.book = Book()

    def search_book_by_genre(self, genre):
        if genre not in BOOK_GENRES:
            print('У нас нет книг такого жанра.')



    def search_book_by_author(self, author):
        if author not in BOOK_AUTHORS:
            print('У нас нет книг этого автора.')


def main():
    pass


if __name__ == '__main__':
    main()




