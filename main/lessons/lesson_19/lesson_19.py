# Занятие 19. ООП. UML, Ассоциации, решение задач


class Transformer:

    def attack(self):
        pass


class AutoBot(Transformer):
    def __init__(self):
        self.left_gun = Gun()
        self.right_gun = Gun()

    def morf(self):
        print('Перевоплащаюсь в машину')

    def attack(self):
        self.left_gun.shoot()
        self.right_gun.shoot()


class Deciptekon(Transformer):
    def __init__(self, left_gun, right_gun):
        self.left_gun = left_gun
        self.right_gun = right_gun

    def morf(self):
        print('Перевоплощаюсь в самолет')

    def attack(self):
        self.left_gun.shoot()
        self.right_gun.shoot()


class Gun:
    def __init__(self):
        self.ammo = 10

    def shoot(self):
        self.ammo -= 1
        print(f'Пушка стреляет, осталось патронов: {self.ammo}')

    def reload(self):
        self.ammo = 10


def main():
    autobot = AutoBot()

    # Ассоциация:
    #   - Композиция
    #   - Агрегация

    left_gun_deciptikon = Gun()
    right_gun_deciptikon = Gun()
    deciptekon = Deciptekon(left_gun_deciptikon, right_gun_deciptikon)


if __name__ == '__main__':
    main()
