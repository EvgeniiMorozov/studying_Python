# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python


def zero(foo=None):
    return 0 if not foo else foo(0)


def one(foo=None):
    return 1 if not foo else foo(1)


def two(foo=None):
    return 2 if not foo else foo(2)


def three(foo=None):
    return 3 if not foo else foo(3)


def four(foo=None):
    return 4 if not foo else foo(4)


def five(foo=None):
    return 5 if not foo else foo(5)


def six(foo=None):
    return 6 if not foo else foo(6)


def seven(foo=None):
    return 7 if not foo else foo(7)


def eight(foo=None):
    return 8 if not foo else foo(8)


def nine(foo=None):
    return 9 if not foo else foo(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


print(nine(divided_by(two())))
