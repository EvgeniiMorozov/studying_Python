import pathlib
import pickle


class Recipe:
    def __init__(self, title, author, course, culinary_cuisine, description, ingredients):
        """
        Рецепт блюда

        :param title: название рецепта
        :param author: автор рецепта
        :param course: тип блюда
        :param culinary_cuisine: принадлежность к кулинарной кухне
        :param description: описание рецепта
        :param ingredients: список ингредиентов
        """
        self.title: str = title
        self.author: str = author
        self.course: str = course
        self.culinary_cuisine: str = culinary_cuisine
        self.description: str = description
        self.ingredients: str = ingredients

    def __repr__(self):
        return f'"{self.title}". {self.course}'


class RecipeDatabase:
    def __init__(self):
        """База рецептов"""
        self.recipes: dict = self.load_data()

    def save_data(self):
        """Сохранение данных в pickle-файл"""
        with open("data.pkl", "wb") as f:
            pickle.dump(self.recipes, f)

    def load_data(self):
        """Загрузка данных из pickle-файла"""
        data_path = pathlib.Path().cwd() / "data.pkl"

        # Если файла не существует, то возвращаем словарь
        if not data_path.exists():
            return dict()

        with open("data.pkl", "rb") as f:
            return pickle.load(f)

    def add_recipe(self, dict_recipe: dict) -> None:
        """Добавление рецепта в базу"""
        recipe = Recipe(*dict_recipe.values())
        self.recipes[recipe.title] = recipe

    def remove_recipe_by_title(self, recipe_title: str) -> None:
        """Удаление рецепта из базы"""
        self.recipes.pop(recipe_title)

    def get_all_recipes(self) -> str:
        """Возвращает все рецепты из базы"""
        return self.recipes.values()

    def get_recipe_by_title(self, recipe_title: str) -> dict:
        """Возвращает рецепт и подробную информацию о нём"""
        recipe = self.recipes[recipe_title]
        detailed_recipe = {
            "Название рецепта": recipe.title,
            "Автор": recipe.author,
            "Тип блюда": recipe.course,
            "Кухня": recipe.culinary_cuisine,
            "Ингредиенты": recipe.ingredients,
            "Описание": recipe.description,
        }
        return detailed_recipe
