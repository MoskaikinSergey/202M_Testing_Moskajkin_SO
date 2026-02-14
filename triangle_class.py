class IncorrectTriangleSides(Exception):
    """Исключение для некорректных сторон треугольника."""
    pass


class Triangle:
    """Класс, описывающий треугольник по длинам трёх сторон."""

    def __init__(self, a, b, c):
        """
        Создаёт треугольник с заданными длинами сторон.
        """
        # Проверка типов
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

        # Проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides(
                f"Нарушено неравенство треугольника: a={a}, b={b}, c={c}"
            )

        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    def triangle_type(self):
        """
        Определяет тип треугольника.
        """
        if self._a == self._b == self._c:
            return "equilateral"
        elif self._a == self._b or self._b == self._c or self._a == self._c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        """
        Вычисляет периметр треугольника.
        """
        return self._a + self._b + self._c

    def __repr__(self):
        return f"Triangle({self._a}, {self._b}, {self._c})"
