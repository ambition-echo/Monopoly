from random import randint


def dice():
    a = randint(1, 6)
    b = randint(1, 6)
    c = a+b
    return a, b, c


if __name__ == '__main__':
    print(dice())
