from product import IProduct


class MustardSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 70

    def __str__(self):
        return "Горчица"


class MayonnaiseSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 80

    def __str__(self):
        return "Майонез"


class KetchupSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Кетчуп"


class GuacamoleSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 95

    def __str__(self):
        return "Гуакамоле"


class DzatzikiSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100

    def __str__(self):
        return "Соус Дзадзики"


class RelishSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100

    def __str__(self):
        return "Релиш"


class SweetChiliSause(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 105

    def __str__(self):
        return "Сладкий Чили"
