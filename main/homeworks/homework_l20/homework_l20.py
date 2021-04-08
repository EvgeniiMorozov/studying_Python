"""
Реализовать иерархию классов согласно приложенной UML-даиграмме.
Она описывает упрощенные элементы популярной игры Counter-Strike,
в которой команда контер-террористов пытается предотвратить планы
террористов.

Есть общий класс Person, от которого наследуются классы Terrorist
и CounterTerrorist. Помимо этого, есть класс Gun, от которого
наследуются AK и M4, каждый из которых состоит в отношении агрегации
соответственно игровой роли (АК для террористов, М4 для контер-террористов).

Реализации стрельбы и перезарядки для каждого класса остаются на усмотрение
разработчика. При желании что-то можно добавить.

В личный кабинет приложить .py файл с реализацией или же ссылку на github
репозиторий.
"""


class Person:
    def __init__(self, health: int):
        self.health = health

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class Gun:
    def __init__(self, ammo: int):
        self.ammo = ammo

        def shoot(self):
            return f"Оружие стреляет"

    def reload(self):
        return f"Оружие перезаряжается"


class CounterTerrorist(Person):
    def __init__(self, health: int):
        super(CounterTerrorist, self).__init__(health)
        self.health = health
        self.gun = M4

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class Terrorist(Person):
    def __init__(self, health: int):
        super(Terrorist, self).__init__(health)
        self.health = health
        self.gun = AK

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class M4(Gun):
    def __init__(self, ammo: int):
        super(M4, self).__init__(ammo)
        self.ammo = ammo

    def shoot(self):
        return f"Винтовка М4 стреляет"


class AK(Gun):
    def __init__(self, ammo: int):
        super(AK, self).__init__(ammo)
        self.ammo = ammo

    def shoot(self):
        return f"Автомат АК стреляет"


def main():
    policeman = CounterTerrorist(100, 50)
    bandit = Terrorist(95, 60)

    policeman.shoot()
    bandit.reload()


if __name__ == "__main__":
    main()
