

from math import acos, pi
from objects.figures import Rect, Triangle, Circle
from objects.types import Point, Vector


def create_point(dimensions: int = 3) -> Point:
    """
    Создать точку
    """
    return Point(dimensions, *[float(input(f"Введите точку в измерении {j} >> ")) for j in range(dimensions)])


def create_vector(dimensions:int = 3) -> Vector:
    """
    Создать вектор
    """
    return Vector(dimensions, create_point(dimensions), create_point(dimensions))


def get_vect_angle(dimensions:int = 3, vector1: Vector = None, vector2: Vector = None) -> float:
    """
    Получить угол между 2 векторами
    """
    poss = sum(map(lambda x: vector1.projection(x) * vector2.projection(x), [*range(dimensions)]))
    lens = abs(vector1) * abs(vector2)
    angle = poss / lens 

    return acos(angle) / pi * 90 * 2 // 0.0000001 / 10000000


def create_triangle(dimensions:int = 3) -> Triangle:
    """
    Создать треугольник
    """

    print("Создание фигуры с типом \"Треугольник\"\n")
    triangle = Triangle(dimensions)

    for i in range(3):
        print(f"Точка {i+1}/3")
        triangle.points[i] = create_point(dimensions)
        print()

    return triangle


def create_rect(dimensions:int = 3) -> Rect:
    """
    Создать прямоугольник
    """

    print("Создание фигуры с типом \"Прямоугольник\"\n")
    rect = Rect(dimensions)

    for i in range(4):
        print(f"Точка {i+1}/4")
        rect.points[i] = create_point(dimensions)
        print()

    storony = map(lambda i: Vector(dimensions, rect.points[i], rect.points[(i+1) % 4]), [*range(4)])
    angles = map(lambda i: get_vect_angle(storony[i], storony[(i+1) % 4]), [*range(4)])

    if set(angles) == {90, }: 
        return rect
        
    else: 
        raise Exception("четырёхугольник должен быть прямоугольным выпуклым!")



def create_circle(dimensions:int = 3) -> Circle:
    """
    Создать окружность
    """

    print("Создание фигуры с типом \"Окружность\"\n")
    return Circle(create_point(dimensions), float(input("Введите радиус окружности >> ")))
