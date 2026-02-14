import pytest
from triangle_class import Triangle, IncorrectTriangleSides


# Позитивные тесты

class TestTriangleCreation:
    """Позитивные тесты создания треугольника."""

    def test_create_equilateral(self):
        """Создание равностороннего треугольника."""
        t = Triangle(5, 5, 5)
        assert t.a == 5
        assert t.b == 5
        assert t.c == 5

    def test_create_isosceles(self):
        """Создание равнобедренного треугольника."""
        t = Triangle(5, 5, 3)
        assert t.a == 5
        assert t.b == 5
        assert t.c == 3

    def test_create_nonequilateral(self):
        """Создание разностороннего треугольника."""
        t = Triangle(3, 4, 5)
        assert t.a == 3
        assert t.b == 4
        assert t.c == 5

    def test_create_float_sides(self):
        """Создание треугольника с дробными сторонами."""
        t = Triangle(3.5, 4.5, 5.5)
        assert t.a == 3.5
        assert t.b == 4.5
        assert t.c == 5.5

    def test_create_small_sides(self):
        """Создание треугольника с очень маленькими сторонами."""
        t = Triangle(0.01, 0.01, 0.01)
        assert t.a == 0.01

    def test_create_large_sides(self):
        """Создание треугольника с очень большими сторонами."""
        t = Triangle(100000, 100000, 100000)
        assert t.a == 100000

class TestTriangleType:
    """Позитивные тесты определения типа треугольника."""

    def test_equilateral_int(self):
        """Равносторонний с целыми сторонами."""
        assert Triangle(5, 5, 5).triangle_type() == "equilateral"

    def test_equilateral_float(self):
        """Равносторонний с дробными сторонами."""
        assert Triangle(3.5, 3.5, 3.5).triangle_type() == "equilateral"

    def test_isosceles_ab(self):
        """Равнобедренный: a == b."""
        assert Triangle(5, 5, 3).triangle_type() == "isosceles"

    def test_isosceles_ac(self):
        """Равнобедренный: a == c."""
        assert Triangle(5, 3, 5).triangle_type() == "isosceles"

    def test_isosceles_bc(self):
        """Равнобедренный: b == c."""
        assert Triangle(3, 5, 5).triangle_type() == "isosceles"

    def test_isosceles_float(self):
        """Равнобедренный с дробными сторонами."""
        assert Triangle(2.5, 2.5, 4).triangle_type() == "isosceles"

    def test_nonequilateral_classic(self):
        """Разносторонний: 3-4-5."""
        assert Triangle(3, 4, 5).triangle_type() == "nonequilateral"

    def test_nonequilateral_int(self):
        """Разносторонний с целыми сторонами."""
        assert Triangle(7, 10, 12).triangle_type() == "nonequilateral"

    def test_nonequilateral_float(self):
        """Разносторонний с дробными сторонами."""
        assert Triangle(2.1, 3.2, 4.3).triangle_type() == "nonequilateral"


class TestPerimeter:
    """Позитивные тесты вычисления периметра."""

    def test_perimeter_equilateral(self):
        """Периметр равностороннего треугольника."""
        assert Triangle(5, 5, 5).perimeter() == 15

    def test_perimeter_isosceles(self):
        """Периметр равнобедренного треугольника."""
        assert Triangle(5, 5, 3).perimeter() == 13

    def test_perimeter_nonequilateral(self):
        """Периметр разностороннего треугольника."""
        assert Triangle(3, 4, 5).perimeter() == 12

    def test_perimeter_float(self):
        """Периметр с дробными сторонами."""
        assert Triangle(1.5, 2.5, 3.0).perimeter() == pytest.approx(7.0)

    def test_perimeter_small(self):
        """Периметр с маленькими сторонами."""
        assert Triangle(0.1, 0.1, 0.1).perimeter() == pytest.approx(0.3)

    def test_perimeter_large(self):
        """Периметр с большими сторонами."""
        assert Triangle(100000, 100000, 100000).perimeter() == 300000


# Незативные тесиы

class TestZeroSides:
    """Негативные тесты: нулевые стороны."""

    def test_zero_a(self):
        """Сторона a равна нулю."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(0, 5, 5)

    def test_zero_b(self):
        """Сторона b равна нулю."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(5, 0, 5)

    def test_zero_c(self):
        """Сторона c равна нулю."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(5, 5, 0)

    def test_zero_all(self):
        """Все стороны равны нулю."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(0, 0, 0)


class TestNegativeSides:
    """Негативные тесты: отрицательные стороны."""

    def test_negative_a(self):
        """Сторона a отрицательна."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(-1, 5, 5)

    def test_negative_b(self):
        """Сторона b отрицательна."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(5, -3, 5)

    def test_negative_c(self):
        """Сторона c отрицательна."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(5, 5, -2)

    def test_negative_all(self):
        """Все стороны отрицательны."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(-1, -1, -1)


class TestTriangleInequality:
    """Негативные тесты: нарушение неравенства треугольника."""

    def test_degenerate(self):
        """Вырожденный: a + b == c."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 3)

    def test_ab_less_than_c(self):
        """a + b < c."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 10)

    def test_bc_less_than_a(self):
        """b + c < a."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(10, 1, 2)

    def test_ac_less_than_b(self):
        """a + c < b."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 10, 2)


class TestInvalidTypes:
    """Негативные тесты: некорректные типы аргументов."""

    def test_string_a(self):
        """Аргумент a — строка."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle("a", 2, 3)

    def test_string_b(self):
        """Аргумент b — строка."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, "b", 5)

    def test_string_c(self):
        """Аргумент c — строка."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 4, "c")

    def test_none(self):
        """Аргумент — None."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle(None, 4, 5)

    def test_list(self):
        """Аргумент — список."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle([3], 4, 5)

    def test_dict(self):
        """Аргумент — словарь."""
        with pytest.raises(IncorrectTriangleSides):
            Triangle({}, 4, 5)
