from math import sqrt
def count_equality(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return "Дискриминант = " + str(d) + " . Корни уравнения: " + str(x1) + " и " + str(x2) + "."
    elif d == 0:
        x = -b / (2 * a)
        return "Дискриминант равен 0. Корень уравнения: " + str(x) + "."
    elif d < 0:
        return "Дискриминант равен " + str(d) + ". Уравнение не имеет действительных корней."