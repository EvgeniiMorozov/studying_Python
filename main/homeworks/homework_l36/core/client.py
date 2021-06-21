class Client:
    """Класс клиента"""
    def __init__(self, name, money):
        self.name = name
        self.money = int(money)

    def get_money(self):
        """Возвращает текущее количество денег"""
        return self.money