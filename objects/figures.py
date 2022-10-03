from functools import reduce
from math import pi

from .types import Point, Figure, Vector


class Triangle(Figure):
    def __init__(self, dimensions = 3, A = None, B = None, C = None):
        self.dimensions = dimensions
        self.points = [
            A or Point(*[0 for i in range(dimensions)]), 
            B or Point(*[0 for i in range(dimensions)]),
            C or Point(*[0 for i in range(dimensions)])
            ]

    def __repr__(self):
        return f"Треугольник с координатами: {', '.join([repr(i) for i in self.points])}"


    def get_area(self) -> int:
        p = self.get_perimeter() / 2
        vector_list = map(lambda i: p - abs(Vector(self.dimensions, self.points[i], self.points[(i+1) % 3])), [*range(3)])
        reduced = reduce(lambda x, y: x*y, vector_list)

        return (p * reduced) ** 0.5 // 0.0000001 / 10000000


class Circle(Figure):
    radius: int


    def __init__(self, dimensions = 3, pos = None, radius = 0):
        self.dimensions = dimensions
        self.points = [pos or Point(*[0 for i in range(dimensions)])]
        self.radius = radius


    def get_area(self) -> int:
        return self.radius ** 2 * pi


    def get_perimeter(self) -> int:
        return self.radius * 2 * pi


    def __repr__(self):
        return f"Окружность с точкой {repr(self.points[0])} и радиусом {self.radius}"
        

class Rect(Figure):
    def __init__(self, dimensions = 3, A = None, B = None, C = None, D = None):
        self.dimensions = dimensions
        self.points = [
            A or Point(*[0 for i in range(dimensions)]), 
            B or Point(*[0 for i in range(dimensions)]),
            C or Point(*[0 for i in range(dimensions)]),
            D or Point(*[0 for i in range(dimensions)])
            ]


    def get_perimeter(self) -> int:
        return super.get_perimeter()


    def get_area(self) -> int:
        triangle1 = Triangle(self.points[0], self.points[1], self.points[2])
        triangle2 = Triangle(self.points[0], self.points[3], self.points[2])
        return triangle1.get_area() + triangle2.get_area()

    
    def output(self):
        return f"Прямоугольник с координатами: {', '.join([repr(i) for i in self.points])}"
