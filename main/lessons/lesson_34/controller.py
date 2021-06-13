from model import ArticleBase
from view import UserInterface


class Controller:
    def __init__(self):
        self.articles_base = ArticleBase()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            self.add_article()
        elif answer == '2':
            self.remove_article()
        elif answer == '3':
            self.show_article()
        elif answer == '4':
            self.show_all_articles()
        elif answer == 'q':
            pass
        else:
            print(f'Действия {answer} не существует!')

    def add_article(self):
        article = self.user_interface.add_user_article()
        self.articles_base.add_article(article)

    def remove_article(self):
        user_title = self.user_interface.get_user_article()
        try:
            self.articles_base.remove_article(user_title)
        except KeyError:
            self.user_interface.show_incorrect_title_error(user_title)

    def show_article(self):
        user_title = self.user_interface.get_user_article()
        article = self.articles_base.get_article_by_title(user_title)
        self.user_interface.show_user_article(article)

    def show_all_articles(self):
        articles = self.articles_base.get_all_articles()
        self.user_interface.user_show_all_articles(articles)
