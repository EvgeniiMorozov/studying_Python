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
    def __init__(self, health):
        self.health = health

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class Gun:
    def __init__(self, ammo):
        self.ammo = ammo

        def shoot(self):
            return f"Оружие стреляет"

    def reload(self):
        return f"Оружие перезаряжается"


class CounterTerrorist(Person):
    def __init__(self, health, gun):
        super(CounterTerrorist, self).__init__(health, gun)
        self.health = health
        self.gun = gun

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class Terrorist(Person):
    def __init__(self, health, gun):
        super(CounterTerrorist, self).__init__(health, gun)
        self.health = health
        self.gun = gun

    def shoot(self):
        return f"Стреляет из оружия"

    def reload(self):
        return f"Перезаряжает оружие"


class M4(Gun):
    def __init__(self, ammo):
        super(M4, self).__init__(ammo)
        self.ammo = ammo

    def shoot(self):
        return f"Винтовка М4 стреляет"   


def main():
    pass


if __name__ == "__main__":
    main()
