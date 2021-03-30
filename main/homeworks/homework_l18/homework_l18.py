"""
Создать класс Дробное число со знаком (Fractions). Число должно быть представлено
двумя полями: целая часть - длинное целое со знаком, дробная часть - беззнаковое
короткое целое. Реализовать арифметические операции сложения, вычитания, умножения
и операции сравнения.
"""


class FractionNum:
    def __init__(self, dec, frac):
        self.decimal = dec
        self.fraction = frac
        # Введём флаг, который будет определять, является ли экземпляр класса отрицательным числом.
        # В дальнейшем нам это понадобится при операциях с дробными частями чисел.
        self.negative = True if self.decimal < 0 else False

    # Переопределим метод __str__
    def __str__(self):
        # {self.fraction:02} -> :02 - желаемая длина строки, в нашем случае 2 символа.
        # Это необходимо, чтоб корректно отражать сотые доли, такие как 0.01, 0.06.
        return f'{self.decimal}.{self.fraction:02}'

    # Сложение десятичных дробей.
    # Целые части чисел мы складываем, а при сложении дробных частей, нам надо
    # ещё учесть знаки чисел, т.к. числа могут быть и отрицательными.
    def __add__(self, other):
        # Целые части чисел мы складываем.
        dec = self.decimal + other.decimal

        # В зависимости от знаков чисел, производим операции с их дробными частями.
        if (not self.negative and not other.negative) or (self.negative and other.negative):
            frac = self.fraction + other.fraction

        elif not self.negative and other.negative:
            frac = self.fraction - other.fraction

        elif self.negative and not other.negative:
            frac = -self.fraction + other.fraction

        frac = abs(frac)
        # по сути у нас максимальное число, которое может получится при сложениии
        # двух дробных частей, при точности вычислений до сотых, это 198. По этому
        # ниже от суммы мы вычитаем 100, а к сумме целых частей прибавляем 1.

        if frac > 100:
            frac -= 100
            dec += 1

        return FractionNum(dec, frac)

    def __sub__(self, other):
        # Целые части чисел мы вычитаем.
        dec = self.decimal - other.decimal

        frac = None
        # В зависимости от знаков чисел, производим операции с их дробными частями.
        if not self.negative and not other.negative:
            frac = self.fraction - other.fraction

        elif not self.negative and other.negative:
            frac = self.fraction + other.fraction

        elif self.negative and not other.negative:
            frac = -self.fraction - other.fraction

        elif self.negative and other.negative:
            frac = -self.negative + other.negative

        frac = abs(frac)

        if frac > 100:
            frac -= 100
            dec = dec - 1 if dec < 0 else dec + 1

        return FractionNum(dec, frac)

    def __mul__(self, other):
        self_str = (str(self.decimal) + str(self.fraction)).strip('-')
        other_str = (str(other.decimal) + str(other.fraction)).strip('-')
        result = 0
        i = 1
        for num in reversed(other_str):
            result += int(self_str) * int(num) * i
            i *= 10
        # print(result)
        dec = result // 10000
        frac = result % 10000

        return FractionNum(dec, frac) if self.negative == other.negative else FractionNum(-dec, frac)


def main():
    float1 = FractionNum(1, 25)
    float2 = FractionNum(3, 76)
    float3 = FractionNum(-5, 77)
    print('Проверка метода __add__')
    print(float1 + float2)
    print(float1 + float3)
    print(float3 + float1)
    print(float2 + float3)

    print('Проверка метода __sub__')
    print(float1 - float2)
    print(float1 - float3)
    print(float3 - float1)
    print(float2 - float3)

    print('Проверка метода __mul__')
    print(float1 * float2)
    print(float1 * float3)
    print(float3 * float1)
    print(float2 * float3)


if __name__ == '__main__':
    main()
