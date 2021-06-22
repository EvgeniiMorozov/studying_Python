from .product import IProduct


class BavarianSausage(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100

    def __str__(self) -> str:
        return "Баварская сосиска"


class SemiSmokedSausage(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 105

    def __str__(self) -> str:
        return "Полукопчёная соситка"


class SoySausage(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 110

    def __str__(self) -> str:
        return "Соевая сосиска"
