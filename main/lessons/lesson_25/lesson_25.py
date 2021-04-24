# Генераторы
def gen_func():
    for i in range(10):
        yield i


def get_fib(n):
    if n in [0, 1]:
        return 1
    else:
        return get_fib(n - 2) + get_fib(n - 1)


def gen_fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        yield b


def sum_fib(n):
    sum = 0
    for i in gen_fib(n):
        sum += i
    return sum


def main():
    # for i in gen_func():
    #     print(i)
    # gen = gen_func()
    # print(gen.__next__())
    # print(gen.__next__())
    # print(gen.__next__())

    # print(get_fib(10))

    # print(list(gen_fib(10)))

    print(sum_fib(1000000))


if __name__ == "__main__":
    main()
