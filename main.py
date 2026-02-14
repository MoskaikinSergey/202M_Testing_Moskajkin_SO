import math

def solve_equation(a, b, c):
    """
    Решает уравнение ax^2 + bx + c = 0.
    """

    # Если все равны нулю
    if a == 0 and b == 0 and c == 0:
        return "Бесконечное множество решений"

    # Если a и b равны нулю
    if a == 0 and b == 0:
        return "Нет решений"

    # Если a = 0 Линейное уравнение
    if a == 0:
        x = -c / b
        return [x]

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return "Нет действительных корней"

    # Если дискриминант равен нулю одно решение
    if discriminant == 0:
        x = -b / (2 * a)
        return [x]

    # Ищем корни
    sqrt_d = math.sqrt(discriminant)
    x1 = (-b - sqrt_d) / (2 * a)
    x2 = (-b + sqrt_d) / (2 * a)

    # Сортируем корни
    if x1 > x2:
        x1, x2 = x2, x1

    return [x1, x2]
