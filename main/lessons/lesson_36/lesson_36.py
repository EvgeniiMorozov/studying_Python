# Занятие 36. Тестирование с PyTest

def add_func(a, b):
    return a + b


def sub_func(a, b):
    return a - b


def mul_func(a, b):
    return a * b


def div_func(a, b):
    return a / b


class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def min(self, a, b):
        return min(a, b)

    def max(self, a, b):
        return max(a, b)

    def percent(self, a, b):
        if not 0<= b <= 1:
            raise ValueError(f'b должно быть от 0 до 1ю Получено: {b}')
        return a * b

    def pow(self, a, b):
        return a ** b


def main():
    pass


if __name__ == '__main__':
    main()
