class Client:
    """Класс клиента"""
    def __init__(self, name, money):
        self.name: str = name
        self.money: int = int(money)

    def get_money(self):
        """Возвращает текущее количество денег"""
        return self.money
