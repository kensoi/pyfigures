from abc import ABC, abstractmethod
from math import sqrt
import typing

class Point:
    x: float
    y: float
    z: float
    dimensions: int


    def __init__(self, dimensions, *args) -> None:
        self.dimensions = dimensions
        self.coordinates = [*args]


    @property
    def x(self):
        return self.coordinates[0]


    @property
    def y(self):
        return self.coordinates[1]


    @property
    def z(self):
        return self.coordinates[2]


    def __repr__(self) -> str:
        return f"({'; '.join(map(str, self.coordinates))})"


class Figure(ABC):
    points: list[Point]
    dimensions: int


    def output(self) -> int:
        """
        Вывод фигуры
        """

        return repr(self)


    def get_perimeter(self) -> int:
        """
        Получить периметр фигуры
        """ 
        return sum(
            map(
                lambda i: abs(Vector(self.points[i], self.points[(i+1) % len(len(self.points))])), 
                [*range(len(self.points))]
                )
            )


    @abstractmethod
    def get_area(self) -> int:
        """
        Получить площадь фигуры
        """

    
    def set_point(self, new_point: Point, index = 0):
        if index >= len(self.points) or index < 0:
            raise Exception("индекс должен быть в пределах [0; 3)")

        self.points = [new_point if i == index else self.points[i] for i in range(len(self.points))]

class Vector(Figure):
    def __init__(self, dimensions = 3, A = None, B = None):
        if not A: A = Point(*[0 for i in range(dimensions)])
        if not B: B = Point(*[0 for i in range(dimensions)])
        self.points = [A, B]
        self.dimensions = dimensions


    def get_len(self):
        # return (self.get_proj("x") ** 2 + self.get_proj("y") ** 2 + self.get_proj("z") ** 2) ** 0.5
        return self.__abs__()

    
    def __abs__(self):
        return sqrt(sum(map(lambda value: value ** 2, [self.get_proj(i) for i in range(self.dimensions)])))


    def get_proj(self, index: typing.Union[int, str]):
        if isinstance(index, str):
            return abs(getattr(self.points[1], index) - getattr(self.points[0], index))
            # self.points[1].x
            # self.points[1].y
            # self.points[1].z

        else:
            return abs(self.points[1].coordinates[index] - self.points[0].coordinates[index])
            # для пространств с любым количеством измерений


    def get_area(self):
        return 0


    def get_perimeter(self):
        return super().get_perimeter()


    def __repr__(self):
        return f"Вектор с координатами: {', '.join(map(repr, self.points))}"

