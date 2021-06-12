# Паттерны проектирования. Поведенческие паттерны.

# Стратегия, Strategy.

class IRouteStrategy:  # Abstract Strategy
    def __init__(self):
        pass

    def build_route(self, a, b, type=None):
        print(f'Строим {type} маршрут от {a} до {b}')


class WalkRoute(IRouteStrategy):  # Concrete Strategy 1
    def __init__(self):
        super().__init__()
        self.type = 'пеший'

    def build_route(self, a, b, type=None):
        super().build_route(a, b, self.type)


class CarRoute(IRouteStrategy):  # Concrete Strategy 2
    def __init__(self):
        super().__init__()
        self.type = 'автомобильный'

    def build_route(self, a, b, type=None):
        super().build_route(a, b, self.type)


class BycicleRoute(IRouteStrategy):  # Concrete Strategy 3
    def __init__(self):
        super().__init__()
        self.type = 'велосипедный'

    def build_route(self, a, b, type=None):
        super().build_route(a, b, self.type)


class MapApplication:  # Context, Контекст.
    def __init__(self):
        self.__strategy = WalkRoute()

    def build_route(self, a, b):
        self.__strategy.build_route(a, b)

    def set_strategy(self, strategy):
        self.__strategy = strategy


# Наблюдатель, Observer.

class ProductDatabase:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for sub in self.subscribers:
            sub.update()


class IStore:
    def __init__(self):
        pass

    def update(self):
        pass


class MagnitStore(IStore):
    def __init__(self):
        super().__init__()
        pass

    def update(self):
        print('Обновился Магнит')


class PaterkaStore(IStore):
    def update(self):
        print('Обновилась пятерочка')


class IkeaStore(IStore):
    def update(self):
        print('Обновилась икея')


def main():
    # Стратегия, Strategy.

    # app = MapApplication()
    # app.build_route('дом', 'работа')
    #
    # app.set_strategy(CarRoute())
    # app.build_route('дом', 'работа')
    #
    # app.set_strategy(BycicleRoute())
    # app.build_route('дом', 'работа')

    # Наблюдатель, Observer.

    database = ProductDatabase()
    magnit = MagnitStore()
    paterka = PaterkaStore()
    ikea = IkeaStore()

    database.subscribe(magnit)
    database.subscribe(paterka)
    database.subscribe(ikea)

    database.notify_subscribers()

    print('-' * 20)

    database.unsubscribe(magnit)
    database.unsubscribe(paterka)

    database.notify_subscribers()


if __name__ == '__main__':
    main()
