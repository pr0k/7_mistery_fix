from math import sqrt

def root(a, b, dis):
    return (-b + dis) / (2 * a)

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return root(a, b, -sqrt(discriminant)), None
    else:
        return root(a, b, -sqrt(discriminant)), root(a, b, sqrt(discriminant))
