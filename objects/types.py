from abc import ABC, abstractmethod
from math import sqrt
import typing

class Point:
    dimensions: int
    coordinates: list[int]


    def __init__(self, dimensions:int=3, *args) -> None:
        self.dimensions = dimensions
        self.coordinates = list(map(int, args))


    def __repr__(self) -> str:
        return f"({'; '.join(map(str, self.coordinates))})"


class Figure(ABC):
    points: list[Point]
    dimensions: int


    def output(self) -> str:
        """
        Вывод фигуры
        """

        return repr(self)


    def get_perimeter(self) -> int:
        """
        Получить периметр фигуры
        """ 

        func = lambda i: abs(Vector(self.dimensions, self.points[i], self.points[(i+1) % len(self.points)]))
        return sum(map(func, [i for i in range(len(self.points))]))


    @abstractmethod
    def get_area(self) -> int:
        """
        Получить площадь фигуры
        """

    
    def set_point(self, new_point: Point = None, index:int = 0) -> None:
        if index >= self.dimensions or index < 0:
            raise Exception(f"индекс должен быть в пределах [0; {self.dimensions})")
        
        self.points[index] = new_point or Point(self.dimensions)


class Vector(Figure):
    def __init__(self, dimensions:int = 3, A:Point = None, B:Point = None) -> None:
        self.points = [A or Point(*[0 for i in range(dimensions)]), B or Point(*[0 for i in range(dimensions)])]
        self.dimensions = dimensions

    
    def __abs__(self) -> float:
        return sqrt(sum(map(lambda value: value ** 2, [self.projection(i) for i in range(self.dimensions)])))


    def projection(self, index: typing.Union[int, str]) -> float:
        return abs(self.points[1].coordinates[index] - self.points[0].coordinates[index])


    def get_area(self) -> int:
        return 0


    def get_perimeter(self) -> float:
        return super().get_perimeter()


    def __repr__(self) -> str:
        return f"Вектор с координатами: {', '.join(map(repr, self.points))}"

