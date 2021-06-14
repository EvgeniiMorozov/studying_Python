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

    def add_recipe(self):
        recipe = {
            "Название рецепта": None,
            "Автор рецепта": None,
            "тип блюда": None,
            "Описание рецепта": None,
            "Ингредиенты": None,
        }

        print(" Добавление рецепта ".center(40, "="))

        for key in recipe:
            recipe[key] = input(f"Введите {key}")

        print("=" * 40)
        return recipe
