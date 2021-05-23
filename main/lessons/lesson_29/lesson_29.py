# Упаковка данных. Pickle
import pickle  # dill - для сериализации лямбда-функций внутри классов


class A:
    c = 3

    def __init__(self):
        self.a = 2
        self.b = 4

    def m1(self, data):
        return self.a + self.b + data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['b']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state
        self.__dict__['l'] = lambda x: x + 1


def main():
    # Хорошая сериализация
    # dct = {i: i for i in range(100)}
    # print(dct)

    # Сериализация в строку и десереализация из строки

    # packed_dct = pickle.dumps(dct)  # консервация/pickling
    # print(packed_dct)
    #
    # unpacked_dct = pickle.loads(packed_dct)
    # print(unpacked_dct)

    # Сериализация в файл и десереализация из файла

    # with open('data.pkl', 'wb') as f:
    #     pickle.dump(dct, f)

    # Pickling пользовательских классов
    # a = A()
    # with open('data.pkl', 'wb') as f:
    #     pickle.dump(a, f)
    #
    # with open('data.pkl', 'rb') as f:
    #     b = pickle.load(f)
    #
    # print(b)
    a = A()
    print(a.__dict__)

    # dct = {i: i for i in range(100)}
    # print(pickle.dumps(dct, protocol=0))


if __name__ == '__main__':
    main()
