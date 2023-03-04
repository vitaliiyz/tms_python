from math import pi, sqrt
from abc import ABC, abstractmethod
from decimal import Decimal


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Figure(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def get_length(a, b):
        return sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


class Circle(Figure):
    __name__ = "Circle"

    def __init__(self, point_1: 'Point', radius_length):
        self._point_1 = point_1
        self._radius_length = radius_length

    @property
    def point_1(self):
        return self._point_1

    @property
    def radius_length(self):
        return self._radius_length

    def perimeter(self):
        circle_perimeter = Decimal(2 * pi * self.radius_length)
        return circle_perimeter.quantize(Decimal("1.00"))

    def area(self):
        circle_square = Decimal(pi * (self.radius_length ** 2))
        return circle_square.quantize(Decimal("1.00"))


class Triangle(Figure):
    __name__ = "Triangle"

    def __init__(self, point_1: 'Point', point_2: 'Point', point_3: 'Point'):
        self._point_1 = point_1
        self._point_2 = point_2
        self._point_3 = point_3

    @property
    def point_1(self):
        return self._point_1

    @property
    def point_2(self):
        return self._point_2

    @property
    def point_3(self):
        return self._point_3

    def get_all_sides(self):
        side_1 = self.get_length(self.point_1, self.point_2)
        side_2 = self.get_length(self.point_2, self.point_3)
        side_3 = self.get_length(self.point_1, self.point_3)

        return side_1, side_2, side_3

    def perimeter(self):
        side_1, side_2, side_3 = self.get_all_sides()
        sum_of_sides = Decimal(side_1 + side_2 + side_3)

        return sum_of_sides.quantize(Decimal("1.00"))

    def area(self):
        semi_perimeter = self.perimeter() / 2
        side_1, side_2, side_3 = map(Decimal, self.get_all_sides())
        triangle_square = Decimal(
            sqrt(semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)))

        return triangle_square.quantize(Decimal("1.00"))


class Square(Figure):
    __name__ = "Square"

    def __init__(self, point_1: 'Point', point_2: 'Point'):
        self._point_1 = point_1
        self._point_2 = point_2

    @property
    def point_1(self):
        return self._point_1

    @property
    def point_2(self):
        return self._point_2

    def get_diagonal_length(self):
        diagonal_length = Decimal(self.get_length(self.point_1, self.point_2))

        return diagonal_length

    def get_side_length(self):
        return self.get_diagonal_length() / Decimal(sqrt(2))

    def perimeter(self):
        square_perimeter = self.get_side_length() * 4

        return square_perimeter.quantize(Decimal("1.00"))

    def area(self):
        square_area = self.get_side_length() ** 2

        return square_area.quantize(Decimal("1.00"))
