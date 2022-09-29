from abc import ABC, abstractmethod

class Point:
    x: int
    y: int
    z: int


    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


    def __repr__(self) -> str:
        return f"({self.x}; {self.y}; {self.z})"


class Figure(ABC):
    points: list[Point]

    @abstractmethod
    def output(self) -> int:
        """
        Вывод фигуры
        """

    @abstractmethod
    def get_perimeter(self) -> int:
        """
        Получить периметр фигуры
        """

    @abstractmethod
    def get_area(self) -> int:
        """
        Получить площадь фигуры
        """

    
    def set_point(self, new_point: Point, index = 0):
        if index >= len(self.points) or index < 0:
            raise Exception("индекс должен быть в пределах [0; 3)")

        self.points = [new_point if i == index else self.points[i] for i in range(len(self.points))]
