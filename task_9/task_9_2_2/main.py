from classes import Point, Circle, Triangle, Square

circle = Circle(Point(3, 3), 10)
triangle = Triangle(Point(1, 1), Point(3, 1), Point(3, 3))
square = Square(Point(1, 1), Point(4, 4))

shapes = [circle, triangle, square]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")
