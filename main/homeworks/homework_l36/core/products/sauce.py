from .product import IProduct


class MustardSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 70

    def __str__(self):
        return "Горчица"


class MayonnaiseSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 80

    def __str__(self):
        return "Майонез"


class KetchupSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Кетчуп"


class GuacamoleSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 95

    def __str__(self):
        return "Гуакамоле"


class DzatzikiSauce(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100

    def __str__(self):
        return "Соус Дзадзики"
