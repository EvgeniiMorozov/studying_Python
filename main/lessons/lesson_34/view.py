class UserInterface:

    def wait_user_answer(self):

        print(' Ввод пользователя '.center(40, '*'))
        print('Что хотим сделать со статьями?')
        print('Возможные варианты:'
              '\n1 - добавить статью'
              '\n2 - удалить статью'
              '\n3 - посмотреть статью'
              '\n4 - посмотреть все статьи'
              '\nq - выйти из программы')

        user_answer = input('Выберите вариант действия: ')
        print('*' * 40)

        return user_answer

    def add_user_article(self):

        dict_article = {
            'Название': None,
            'Автор': None,
            'Количество страниц': None,
            'Источник': None,
            'Описание': None,
        }
        print(' Добавление статьи '.center(40, '*'))

        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        print('*' * 40)
        return dict_article

    def get_user_article(self):

        print(' Введите название статьи '.center(40, '*'))
        user_title = input('Введите название статьи: ')
        print('*' * 40)

        return user_title

    def show_user_article(self, article: dict):
        print(' Информация о статье '.center(40, '*'))

        for key in article:
            print(f'{key} статьи:\n{article[key]}')

        print('*' * 40)

    def user_show_all_articles(self, articles: list):
        print(' Все статьи '.center(40, '*'))

        for idx, article in enumerate(articles, start=1):
            print(f'{idx}. {article}')

        print('*' * 40)

    def show_incorrect_title_error(self, title):
        print(' ОШИБКА: Неправильное название статьи! '.center(40, '*'))
        print(f' Статьи {title} не существует!')
        print('*' * 40)
