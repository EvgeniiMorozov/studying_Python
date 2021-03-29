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

    # Переопределим метод __str__
    def __str__(self):
        # {self.fraction:2} -> :2 - желаемая длина строки, в нашем случае 2 символа.
        # Это необходимо, чтоб корректно отражать сотые доли, такие как 0.01, 0.06.
        return f'{self.decimal}.{self.fraction:2}'

    def __add__(self, other):
        dec = self.decimal + other.decimal
        frac = self.fraction + other.fraction

        # по сути у нас максимальное число, которое может получится при сложениии
        # двух дробных частей, при точности вычислений до сотых, это 198. По этому
        # ниже от суммы мы вычитаем 100, а к сумме целых частей прибавляем 1.
        if frac > 100:
            frac -= 100
            dec += 1

        return FractionNum(dec, frac)


def main():
    float1 = FractionNum(1, 25)
    float2 = FractionNum(3, 76)
    float3 = FractionNum(-5, 77)
    print(float1 + float2)


if __name__ == '__main__':
    main()
