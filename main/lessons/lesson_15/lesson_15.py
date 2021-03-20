# Collections.
import collections
import time


class Car:
    def __init__(self, model, count_wheels, count_doors):
        self.model = model
        self.count_wheels = count_wheels
        self.count_doors = count_doors

    def drive(self):
        print(f'Машина {self.model} поехала на {self.count_wheels} колёсах и с {self.count_doors} дверьми')


def main():
    # Collections.
    # defaultdict()
    dct = {'1': 1, '2': 2, '3': 5}
    default_dict = collections.defaultdict(int)
    # default_dict = {'1': 1, '2': 2, '3': 5}

    for i in range(10):
        # if str(i) in dct:
        #     dct[str(i)] += 1
        default_dict[str(i)] += 1
        # else:
        #     dct[str(i)] = 1
    # print(default_dict)

    # ChainMap()

    cats = {'Bob': 1, 'Marvin': 2, 'Snejok': 5}
    dogs = {'Rex': 3, 'Jon': 4, 'Bobik': 1}
    horses = {'Rubin': 5, 'Strela': 6, 'Bistraya': 3}

    animals = collections.ChainMap(cats, dogs, horses)
    # print(animals)
    # print(animals['Bob'])

    # меняем всех животных по отдельности
    cats['Bob'] = 2
    dogs['Rex'] = 6
    horses['Rubin'] = 9

    # print(animals)
    # animals['Bob'] = 12
    # print(animals)
    # print(cats)

    # deque

    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # arr = [i for i in range(1000000)]
    # deq = collections.deque(arr)
    # print(arr, arr.__sizeof__())
    # print(deq, deq.__sizeof__())
    #
    # arr.append(11)
    # print(arr)
    #
    # deq.append(11)
    # print(deq)
    #
    # arr.insert(0, 0)
    # print(arr)
    #
    # deq.appendleft(0)
    # print(deq)

    # namedtuple()

    # params = ['age', 'weight', 'height']
    # User = collections.namedtuple('User', params)
    # Vasya = User(12, 70, 180)
    # print(Vasya)
    # print(Vasya.age)
    # # Vasya.age = 20
    # # print(Vasya)  # AttributeError: can't set attribute
    #
    # Petya = User(20, 80, 160)
    # print(Petya)

    # OOP

    car1 = Car('Toyota', 4, 4)
    car2 = Car('Жигули', 1, 1)
    print(car1)
    car1.drive()
    car2.drive()


if __name__ == '__main__':
    main()

