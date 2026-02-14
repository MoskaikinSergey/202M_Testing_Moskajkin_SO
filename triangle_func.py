class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


def get_triangle_type(a, b, c):
    """
    Определяет тип треугольника по длинам сторон.
        a, b, c — длины сторон треугольника
        "equilateral"    — равносторонний (все стороны равны)
        "isosceles"      — равнобедренный (две стороны равны)
        "nonequilateral" — разносторонний (все стороны различны)

    Позитивные тесты

    Равносторонний треугольник (целые):
    >>> get_triangle_type(5, 5, 5)
    'equilateral'

    Равносторонний треугольник (дробные):
    >>> get_triangle_type(3.5, 3.5, 3.5)
    'equilateral'

    Равносторонний треугольник (очень маленькие стороны):
    >>> get_triangle_type(0.01, 0.01, 0.01)
    'equilateral'

    Равносторонний треугольник (очень большие стороны):
    >>> get_triangle_type(100000, 100000, 100000)
    'equilateral'

    Равнобедренный: a == b:
    >>> get_triangle_type(5, 5, 3)
    'isosceles'

    Равнобедренный: a == c:
    >>> get_triangle_type(5, 3, 5)
    'isosceles'

    Равнобедренный: b == c:
    >>> get_triangle_type(3, 5, 5)
    'isosceles'

    Равнобедренный с дробными равными сторонами:
    >>> get_triangle_type(2.5, 2.5, 4)
    'isosceles'

    Равнобедренный, третья сторона близка к сумме двух других:
    >>> get_triangle_type(1, 1, 1.999)
    'isosceles'

    Разносторонний (прямоугольный 3-4-5):
    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'

    Разносторонний (целые):
    >>> get_triangle_type(7, 10, 12)
    'nonequilateral'

    Разносторонний (дробные):
    >>> get_triangle_type(2.1, 3.2, 4.3)
    'nonequilateral'

    Негативные тесты

    Сторона a равна нулю:
    >>> get_triangle_type(0, 5, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=0, b=5, c=5

    Сторона b равна нулю:
    >>> get_triangle_type(5, 0, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=5, b=0, c=5

    Сторона c равна нулю:
    >>> get_triangle_type(5, 5, 0)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=5, b=5, c=0

    Все стороны равны нулю:
    >>> get_triangle_type(0, 0, 0)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=0, b=0, c=0

    Сторона a отрицательна:
    >>> get_triangle_type(-1, 5, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=-1, b=5, c=5

    Сторона b отрицательна:
    >>> get_triangle_type(5, -3, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=5, b=-3, c=5

    Сторона c отрицательна:
    >>> get_triangle_type(5, 5, -2)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=5, b=5, c=-2

    Все стороны отрицательны:
    >>> get_triangle_type(-1, -1, -1)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Стороны должны быть положительными: a=-1, b=-1, c=-1

    Нарушение неравенства треугольника (вырожденный, a + b == c):
    >>> get_triangle_type(1, 2, 3)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Нарушено неравенство треугольника: a=1, b=2, c=3

    Нарушение неравенства треугольника (a + b < c):
    >>> get_triangle_type(1, 2, 10)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Нарушено неравенство треугольника: a=1, b=2, c=10

    Нарушение неравенства треугольника (b + c < a):
    >>> get_triangle_type(10, 1, 2)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Нарушено неравенство треугольника: a=10, b=1, c=2

    Нарушение неравенства треугольника (a + c < b):
    >>> get_triangle_type(1, 10, 2)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Нарушено неравенство треугольника: a=1, b=10, c=2

    Аргумент a — строка:
    >>> get_triangle_type("a", 2, 3)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Сторона 'a' не является числом

    Аргумент b — строка:
    >>> get_triangle_type(3, "b", 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Сторона 'b' не является числом

    Аргумент c — строка:
    >>> get_triangle_type(3, 4, "c")
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Сторона 'c' не является числом

    Аргумент a — None:
    >>> get_triangle_type(None, 4, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Сторона 'None' не является числом

    Аргумент a — список:
    >>> get_triangle_type([3], 4, 5)
    Traceback (most recent call last):
        ...
    triangle_func.IncorrectTriangleSides: Сторона '[3]' не является числом
    """

    # Проверка типов: должны быть числа (int или float)
    for side in (a, b, c):
        if isinstance(side, bool) or not isinstance(side, (int, float)):
            raise IncorrectTriangleSides(
                f"Сторона '{side}' не является числом"
            )

    # Проверка на положительность
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides(
            f"Стороны должны быть положительными: a={a}, b={b}, c={c}"
        )

    # Проверка неравенства треугольника: сумма любых двух сторон должна быть строго больше третьей
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides(
            f"Нарушено неравенство треугольника: a={a}, b={b}, c={c}"
        )

    # Определяем тип
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
