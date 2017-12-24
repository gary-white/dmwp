__author__ = 'garywhite'


def roots(a, b, c):
    d = (b ** 2 - 4 * a * c) ** (1 / 2)
    x_1 = (-b + d) / (2 * a)
    x_2 = (-b - d) / (2 * a)
    return x_1, x_2


print(roots(float(1), float(1), float(1)))
