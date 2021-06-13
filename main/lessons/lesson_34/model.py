class Article:
    def __init__(self, title, author, pages, publish_source, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.publish_source = publish_source
        self.description = description

    def __repr__(self):
        return f'{self.author}. "{self.title}"'


class ArticleBase:
    def __init__(self):
        self.articles: dict = {}

    def add_article(self, dict_article: dict):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def remove_article(self, title: str):
        self.articles.pop(title)

    def get_article_by_title(self, user_title):
        article = self.articles[user_title]
        article_dict = {
            'Название': article.title,
            'Автор': article.author,
            'Количество страниц': article.pages,
            'Источник': article.publish_source,
            'Описание': article.description,
        }
        return article_dict

    def get_all_articles(self):
        return self.articles.values()
