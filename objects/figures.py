from math import acos, pi
from .types import Point, Figure


class Vector(Figure):
    def __init__(self, A = Point(0,0,0), B = Point(0,0,0)):
        self.points = [A, B]


    def get_len(self):
        return (self.get_proj("x") ** 2 + self.get_proj("y") ** 2 + self.get_proj("z") ** 2) ** 0.5


    def get_proj(self, index: str):
        return abs(getattr(self.points[1], index) - getattr(self.points[0], index))


    def get_area(self):
        return 0


    def get_perimeter(self):
        return self.get_len() * 2


    def output(self):
        return f"Вектор с координатами: {', '.join([repr(i) for i in self.points])}"


def get_vect_angle(v1: Vector, v2: Vector):
    poss = v1.get_proj("x") * v2.get_proj("x") + v1.get_proj("y") * v2.get_proj("y") + v1.get_proj("z") * v2.get_proj("z")
    lens = v1.get_len() * v2.get_len()
    angle = poss / lens

    return acos(angle) / pi * 90 * 2 // 0.0000001 / 10000000


class Triangle(Figure):
    def __init__(self, A = Point(0,0,0), B = Point(0,0,0), C = Point(0,0,0)):
        self.points = [A, B, C]

    
    def get_perimeter(self) -> int:
        AB = Vector(self.points[0], self.points[1])
        BC = Vector(self.points[1], self.points[2])
        CA = Vector(self.points[2], self.points[0])

        return AB.get_len() + BC.get_len() + CA.get_len()


    def get_area(self) -> int:
        p = self.get_perimeter() / 2
        
        AB = Vector(self.points[0], self.points[1])
        BC = Vector(self.points[1], self.points[2])
        CA = Vector(self.points[2], self.points[0])

        return (p * (p - AB.get_len()) * (p - BC.get_len()) * (p - CA.get_len())) ** 0.5


    def output(self):
        return f"Треугольник с координатами: {', '.join([repr(i) for i in self.points])}"


class Round(Figure):
    radius: int


    def __init__(self, pos = Point(0,0,0), radius = 0):
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
    def __init__(self, A = Point(0,0,0), B = Point(0,0,0), C = Point(0,0,0), D = Point(0,0,0)):
        self.points = [A, B, C, D]


    def get_perimeter(self) -> int:
        AB = Vector(self.points[0], self.points[1])
        BC = Vector(self.points[1], self.points[2])
        CD = Vector(self.points[2], self.points[3])
        DA = Vector(self.points[3], self.points[0])

        return AB.get_len() + BC.get_len() + CD.get_len() + DA.get_len()


    def get_area(self) -> int:
        AB = Vector(self.points[0], self.points[1])
        BC = Vector(self.points[1], self.points[2])
        
        s = AB.get_len() * BC.get_len()
        return s

    
    def output(self):
        return f"Прямоугольник с координатами: {', '.join([repr(i) for i in self.points])}"
