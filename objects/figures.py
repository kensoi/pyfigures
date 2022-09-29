from functools import reduce
from math import pi

from .types import DIMENSIONS, Point, Figure, Vector


class Triangle(Figure):
    def __init__(self, 
            A = Point(*[0 for i in range(DIMENSIONS)]), 
            B = Point(*[0 for i in range(DIMENSIONS)]), 
            C = Point(*[0 for i in range(DIMENSIONS)])):
        self.points = [A, B, C]

    
    def get_perimeter(self) -> int:
        # AB = Vector(self.points[0], self.points[1]) # Вектор от точки А до точки B
        # BC = Vector(self.points[1], self.points[2]) # Вектор от точки B до точки C
        # CA = Vector(self.points[2], self.points[0]) # Вектор от точки C до точки A

        # Vector(A, B).get_len() = получить модуль вектора, хотя можно было просто abs(Vector(A, B))

        # return AB.get_len() + BC.get_len() + CA.get_len() # Сумма модулей этих векторов = периметр треугольника.
        
        return sum(
            map(
                lambda i: abs(Vector(self.points[i], self.points[(i+1) % len(self.points)])), 
                [*range(len(self.points))]
                )
            )


    def get_area(self) -> int:
        p = self.get_perimeter() / 2
        
        AB = Vector(self.points[0], self.points[1])
        BC = Vector(self.points[1], self.points[2])
        CA = Vector(self.points[2], self.points[0])
        reduced = reduce(lambda x, y: x*y, map(lambda i: p - abs(Vector(self.points[i], self.points[(i+1) % 3])), [*range(3)]))

        return (p * reduced) ** 0.5 // 0.0000001 / 10000000


    def output(self):
        return f"Треугольник с координатами: {', '.join([repr(i) for i in self.points])}"


class Round(Figure):
    radius: int


    def __init__(self, pos = Point(*[0 for i in range(DIMENSIONS)]), radius = 0):
        self.points = [pos]
        self.radius = radius

    
    def set_pos(self, point):
        self.points = [point]


    def get_area(self) -> int:
        return self.radius ** 2 * pi


    def get_perimeter(self) -> int:
        return self.radius * 2 * pi


    def output(self):
        return f"Окружность с точкой {repr(self.points[0])} и радиусом {self.radius}"
        

class Rectangular(Figure):
    def __init__(self, 
            A = Point(*[0 for i in range(DIMENSIONS)]), 
            B = Point(*[0 for i in range(DIMENSIONS)]), 
            C = Point(*[0 for i in range(DIMENSIONS)]), 
            D = Point(*[0 for i in range(DIMENSIONS)])):
        self.points = [A, B, C, D]


    def get_perimeter(self) -> int:
        # AB = Vector(self.points[0], self.points[1])
        # BC = Vector(self.points[1], self.points[2])
        # CD = Vector(self.points[2], self.points[3])
        # DA = Vector(self.points[3], self.points[0])

        # return AB.get_len() + BC.get_len() + CD.get_len() + DA.get_len()
        return super.get_perimeter()


    def get_area(self) -> int:
        triangle1 = Triangle(self.points[0], self.points[1], self.points[2])
        triangle2 = Triangle(self.points[0], self.points[3], self.points[2])
        return triangle1.get_area() + triangle2.get_area()

    
    def output(self):
        return f"Прямоугольник с координатами: {', '.join([repr(i) for i in self.points])}"
