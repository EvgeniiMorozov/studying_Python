from .product import IProduct


class MushroomTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 65

    def __str__(self):
        return 'грибы'


class CucumberTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 45

    def __str__(self):
        return 'огурцы'


class ChiliTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 75

    def __str__(self):
        return 'перец чили'


class CheeseTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 80

    def __str__(self):
        return 'сыр'

    def __repr__(self):
        return 'сыр'


