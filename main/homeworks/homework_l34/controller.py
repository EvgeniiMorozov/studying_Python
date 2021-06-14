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

    def quit(self):
        pass
