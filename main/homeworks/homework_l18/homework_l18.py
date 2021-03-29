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

    def __str__(self):
        return f'{self.decimal}.{self.fraction}'

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
