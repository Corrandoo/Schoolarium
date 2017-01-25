from math import sqrt
def count_equality(a, b, c):
    d = b ** 2 - 4 * a * c
    returnings = []
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        returnings.append(x1)
        returnings.append(x2)
    elif d == 0:
        x = -b / (2 * a)
        returnings.append(x)
    elif d < 0:
        returnings.append("none")
    return returnings