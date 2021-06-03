from abc import ABC, abstractmethod


# Паттерны проектирования. Порождающие паттерны.

# Фабричный метод, Factory Method, Виртуальный конструктор.

# Creator
class Logistics:

    @abstractmethod
    def create_transport(self):
        pass


# Concrete_Creator_1
class GroundLogistic(Logistics):

    def create_transport(self):
        return Truck()


# Concrete_Creator_2
class SeaLogistic(Logistics):
    def create_transport(self):
        return Ship()


class AirLogistic(Logistics):
    def create_transport(self):
        return Aircraft()


# Interface (Интерфейс)
class ITransport:

    def deliver(self):
        pass


class Truck(ITransport):
    def deliver(self):
        print('Доставка по суше')


class Ship(ITransport):
    def deliver(self):
        print('Доставка по морю')


class Aircraft(ITransport):
    def deliver(self):
        print('Доставка по воздуху')


# Абстрактная фабрика, Фабрика, Abstract Factory, Factory.

# Creator
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


# Concrete_Creator_1
class OldFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return OldChair()

    def create_table(self):
        return OldTable()


# Concrete_Creator_2
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()


class IChair:
    def sit(self):
        pass


class OldChair(IChair):
    def sit(self):
        print('Сидим на старом стуле')


class ModernChair(IChair):
    def sit(self):
        print('Сидим на современном стуле')


class ITable:
    def eat(self):
        pass


class OldTable(ITable):
    def eat(self):
        print('Кушаем за старым столом')


class ModernTable(ITable):
    def eat(self):
        print('Кушаем за современным столом')


def main():

    # Фабричный метод, Factory Method, Виртуальный конструктор.

    # ground_logistic = GroundLogistic()
    # sea_logistic = SeaLogistic()
    # air_logistic = AirLogistic()
    #
    # truck1 = ground_logistic.create_transport()
    # ship1 = sea_logistic.create_transport()
    # aircraft1 = air_logistic.create_transport()
    #
    # truck1.deliver()
    # ship1.deliver()
    # aircraft1.deliver()

    # Абстрактная фабрика, Фабрика, Abstract Factory, Factory.

    old_furniture_factory = OldFurnitureFactory()
    modern_furniture_factory = ModernFurnitureFactory()

    old_chair = old_furniture_factory.create_chair()
    old_table = old_furniture_factory.create_table()
    modern_table = modern_furniture_factory.create_table()

    old_table.eat()
    old_chair.sit()
    modern_table.eat()


if __name__ == '__main__':
    main()
