from math import sqrt

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return (-b - sqrt(discriminant)) / (2 * a), None
    else:
        return (-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)
