from product import IProduct


class RelishTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 100

    def __str__(self):
        return "Релиш"


class SweetChiliTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 105

    def __str__(self):
        return "Сладкий Чили"


class SweetPeperTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Сладкий перец"


class CabbageTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 85

    def __str__(self):
        return "Капуста"


class TomatoTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 85

    def __str__(self):
        return "Помидоры"


class OnionTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 75

    def __str__(self):
        return "Лук"


class FreshVegetablesTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Свежие овощи"


class PickledCucumberTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Маринованный огурчик"


class JalapenoTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Халапеньо"


class ChiliTopping(IProduct):
    def __init__(self):
        super().__init__()
        self.price = 90

    def __str__(self):
        return "Чили"
