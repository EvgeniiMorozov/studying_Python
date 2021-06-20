from .product import IProduct


class BeefMeat(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 150

    def __str__(self):
        return 'баранина'


class PorkMeat(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 145

    def __str__(self):
        return 'свинина'


class SalamiMeat(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 115

    def __str__(self):
        return 'салями'
