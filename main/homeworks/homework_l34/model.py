class Recipe:
    def __init__(self, title, author, course, food_type, description, ingredients):
        self.title: str = title
        self.author: str = author
        self.course: str = course
        self.food_type: str = food_type
        self.description: str = description
        self.ingredients: str = ingredients

    def __repr__(self):
        return f'"{self.title}". {self.course}'


class RecipeDatabase:
    def __init__(self):
        self.recipes: dict = dict()

    def add_recipe(self, dict_recipe: dict) -> None:
        recipe = Recipe(*dict_recipe.values())
        self.recipes[recipe.title] = recipe

    def safe_quit(self):
        pass
