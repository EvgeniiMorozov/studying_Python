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


BOOK_GENRES = ['Фэнтези', 'Научная фантастика', 'Приключения', 'Драма', 'Детектив', 'Поэзия']
BOOK_AUTHORS = [
    'Иван Иванов',
    'Андрей Андреев',
    'Василий Васильев',
    'Дмитрий Дмитриев',
    'Григорий Григорьев',
    'Михаил Михайлов'
]
BOOK_NAMES = [
    'Природа смешариков',
    'Шварц против Сталлоне',
    'Восстание телепузиков',
    'Смешарики наносит ответный удар',
    'Старая надежда',
    'В поисках Джеки Чана',
    'Атака телепузиков',
    'Мистер Андерсон'
]


class Book:
    def __init__(self):
        self.author: str = str()
        self.genre: str = str()
        self.name: str = str()

    def __str__(self) -> str:
        info = f'Эта книга называется: {self.name},\n' \
               f'написал её выдающийся автор: {self.author},\n' \
               f'непревзойдённый мастер жанра {self.genre}.'
        return info

    def __del__(self):
        return 'Библиотекарь поставил книжку на полку.'


class Reader:
    def __init__(self, name):
        self.__name: str = name

    # Изначально хотел сделать метод, который возвращает экземпляр читателя и жанр книги, но не получилось.

    # def choose_book(self, genre: str):
    #     print(f'Читатель {self.__name} хочет почитать что-нибудь из {genre}.')
    #     return Reader, genre

    def choose_book(self, genre: str):
        print(f'Читатель {self.__name} хочет почитать что-нибудь из {genre}.')
        return genre

    def read_book(self, book: str):
        print(f'Читатель {self.__name} читает книгу {book}.')

    def get_name(self) -> str:
        return self.__name

    def __del__(self):
        print(f'Довольный читатель {self.__name} покинул библиотеку.')


class Librarian:
    def __init__(self):
        self.book = None

    def add_book(self, genre: str) -> Book:
        """ Метод, создающий экземпляр книги. """
        self.book = Book()
        self.book.genre = genre
        self.book.author = choice(BOOK_AUTHORS)
        self.book.name = choice(BOOK_NAMES)
        return self.book

    def change_book(self):
        pass

    def give_book(self, reader: Reader, book: Book):
        """ Метод, ответственный за выдачу книги читателю. """
        print(f'Библиотекарь выдаёт книгу "{book.name}" читателю {reader.get_name()}.')

    def delete_book(self, book: Book):
        """ Метод, удаляющий экземпляр книги. """
        print('Библиотекарь забрал книгу у читателя. ' + book.__del__())

    # def __del__(self):
    #     return f'Библиотекарь взглянул на часы и начал собираться домой.'


class LibraryFacade:
    def __init__(self):
        self.librarian = Librarian()
        self.book = None

    def take_order(self, reader: Reader, genre: str):
        self.search_book_by_genre(reader, genre)
        reader.read_book(self.book)

    def reader_returns_book(self):
        self.librarian.delete_book(self.book)

    def search_book_by_genre(self, reader, genre):
        """Поиск книги по жанру."""
        if genre not in BOOK_GENRES:
            print(f'У нас нет книг такого жанра. Но книга "{choice(BOOK_NAMES)}" очень интересная, советуем прочитать.')
        else:
            self.book = self.librarian.add_book(genre)
            self.librarian.give_book(reader, self.book)

    # def __del__(self):
    #     return f'Библиотека закрывается.'


def main():
    library = LibraryFacade()

    reader1 = Reader('Геннадий')
    choice1 = reader1.choose_book('Фэнтези')
    library.take_order(reader1, choice1)
    library.reader_returns_book()

    # reader2 = Reader('Станислав')
    # choice2 = reader2.choose_book('Мистика')
    # library.search_book_by_genre(reader2, choice2)


if __name__ == '__main__':
    main()




