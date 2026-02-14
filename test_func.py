import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestEquilateral(unittest.TestCase):
    """Тесты для равностороннего треугольника."""

    def test_equilateral_int(self):
        """Равносторонний треугольник с целыми сторонами."""
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")

    def test_equilateral_float(self):
        """Равносторонний треугольник с дробными сторонами."""
        self.assertEqual(get_triangle_type(3.5, 3.5, 3.5), "equilateral")

    def test_equilateral_small(self):
        """Равносторонний треугольник с очень маленькими сторонами."""
        self.assertEqual(get_triangle_type(0.01, 0.01, 0.01), "equilateral")

    def test_equilateral_large(self):
        """Равносторонний треугольник с очень большими сторонами."""
        self.assertEqual(get_triangle_type(100000, 100000, 100000), "equilateral")


class TestIsosceles(unittest.TestCase):
    """Тесты для равнобедренного треугольника."""

    def test_isosceles_ab_equal(self):
        """Равнобедренный: a == b."""
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")

    def test_isosceles_ac_equal(self):
        """Равнобедренный: a == c."""
        self.assertEqual(get_triangle_type(5, 3, 5), "isosceles")

    def test_isosceles_bc_equal(self):
        """Равнобедренный: b == c."""
        self.assertEqual(get_triangle_type(3, 5, 5), "isosceles")

    def test_isosceles_float(self):
        """Равнобедренный с дробными равными сторонами."""
        self.assertEqual(get_triangle_type(2.5, 2.5, 4), "isosceles")

    def test_isosceles_near_degenerate(self):
        """Равнобедренный, третья сторона близка к сумме двух других."""
        self.assertEqual(get_triangle_type(1, 1, 1.999), "isosceles")


class TestNonequilateral(unittest.TestCase):
    """Тесты для разностороннего треугольника."""

    def test_nonequilateral_classic(self):
        """Разносторонний (прямоугольный 3-4-5)."""
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    def test_nonequilateral_int(self):
        """Разносторонний с целыми сторонами."""
        self.assertEqual(get_triangle_type(7, 10, 12), "nonequilateral")

    def test_nonequilateral_float(self):
        """Разносторонний с дробными сторонами."""
        self.assertEqual(get_triangle_type(2.1, 3.2, 4.3), "nonequilateral")


class TestZeroSides(unittest.TestCase):
    """Тесты с нулевыми сторонами."""

    def test_zero_a(self):
        """Сторона a равна нулю."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 5, 5)

    def test_zero_b(self):
        """Сторона b равна нулю."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 0, 5)

    def test_zero_c(self):
        """Сторона c равна нулю."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 5, 0)

    def test_zero_all(self):
        """Все стороны равны нулю."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)


class TestNegativeSides(unittest.TestCase):
    """Тесты с отрицательными сторонами."""

    def test_negative_a(self):
        """Сторона a отрицательна."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 5, 5)

    def test_negative_b(self):
        """Сторона b отрицательна."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, -3, 5)

    def test_negative_c(self):
        """Сторона c отрицательна."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 5, -2)

    def test_negative_all(self):
        """Все стороны отрицательны."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -1, -1)


class TestTriangleInequality(unittest.TestCase):
    """Тесты на нарушение неравенства треугольника."""

    def test_degenerate(self):
        """Вырожденный: a + b == c."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    def test_ab_less_than_c(self):
        """a + b < c."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 10)

    def test_bc_less_than_a(self):
        """b + c < a."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 2)

    def test_ac_less_than_b(self):
        """a + c < b."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 10, 2)


class TestInvalidTypes(unittest.TestCase):
    """Тесты с некорректными типами аргументов."""

    def test_string_a(self):
        """Аргумент a — строка."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("a", 2, 3)

    def test_string_b(self):
        """Аргумент b — строка."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, "b", 5)

    def test_string_c(self):
        """Аргумент c — строка."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, "c")

    def test_none(self):
        """Аргумент a — None."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(None, 4, 5)

    def test_list(self):
        """Аргумент a — список."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type([3], 4, 5)

    def test_bool(self):
        """Аргумент a — bool."""
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(True, 2, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
