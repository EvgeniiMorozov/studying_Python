class UserInterface:
    def wait_user_answer(self):
        print(" Ввод пользователя ".center(40, "="))
        print("Что будем делать с рецептами?")
        print(
            "Возможные действия:"
            "\n1 - добавить рецепт"
            "\n2 - удалить рецепт"
            "\n3 - посмотреть рецепт"
            "\n4 - посмотреть все рецепты"
            "\nq - выйти из программы"
        )

        user_answer = input("Выберите вариант действия: ")
        print("=" * 40)
        return user_answer

    @staticmethod
    def say_bay():
        print(" До скорых встреч! ".center(40, "="))

    def add_recipe(self) -> dict:
        recipe = {
            "Название рецепта": None,
            "Автор рецепта": None,
            "тип блюда": None,
            "Кулинарная кухня": None,
            "Описание рецепта": None,
            "Ингредиенты": None,
        }

        print(" Добавление рецепта ".center(40, "="))

        for key in recipe:
            recipe[key] = input(f"Введите {key}: ")

        print("=" * 40)
        return recipe

    def get_recipe_by_title(self) -> str:
        print(" Выбор рецепта ".center(40, "="))
        recipe_title = input("Введите название рецепта: ")
        print("=" * 40)
        return recipe_title

    def show_all_recipes(self, recipes: list) -> None:
        print(" Рецепты: ".center(40, "="))

        if not recipes:
            print("Рецептов нет!")

        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}) {recipe}")

        print('=' * 40)

    def show_user_recipe(self, recipe: dict) -> None:
        print(" Информация о рецепте ".center(40, "="))

        for key in recipe:
            print(f"{key}: {recipe[key]}")

        print('=' * 40)
