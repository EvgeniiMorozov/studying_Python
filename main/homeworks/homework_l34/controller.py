from model import RecipeDatabase
from view import UserInterface


class Controller:
    def __init__(self) -> None:
        self.recipes_base = RecipeDatabase()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "q":
            self.quit()
        elif answer == "1":
            self.add_recipe()
        elif answer == "2":
            self.remove_recipe()
        elif answer == "3":
            self.show_all_recipes()

    def quit(self):
        """Корректный выход из программы"""
        self.recipes_base.save_data()
        self.user_interface.say_bay()

    def add_recipe(self):
        """Добавление рецепта"""
        recipe = self.user_interface.add_recipe()
        self.recipes_base.add_recipe(recipe)

    def remove_recipe(self):
        """Удаление рецепта"""
        recipe_title = self.user_interface.get_recipe_by_title()
        self.recipes_base.remove_recipe_by_title(recipe_title)

    def show_all_recipes(self):
        """Показать все рецепты"""
        recipes = self.recipes_base.get_all_recipes()
        self.user_interface.show_all_recipes(recipes)
