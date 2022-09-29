

from math import acos, pi
from objects.figures import Rect, Triangle, Circle
from objects.types import Point, Vector


def create_point(dimensions = 3):
    """
    Создать точку
    """
    return Point(dimensions, *[float(input(f"Введите точку в измерении {j} >> ")) for j in range(dimensions)])


def create_vector(dimensions = 3):
    """
    Создать вектор
    """
    return Vector(dimensions, create_point(dimensions), create_point(dimensions))


def get_vect_angle(v1: Vector, v2: Vector) -> float:
    """
    Получить угол между 2 векторами
    """
    poss = sum(map(lambda x: v1.get_proj(x) * v2.get_proj(x), [*range(v1.dim)]))
    lens = abs(v1) * abs(v2)
    angle = poss / lens 

    return acos(angle) / pi * 90 * 2 // 0.0000001 / 10000000


def create_triangle(dimensions = 3) -> Triangle:
    """
    Создать треугольник
    """

    print("Создание фигуры с типом \"Треугольник\"\n")
    triangle = Triangle(dimensions)

    for i in range(3):
        print(f"Точка №{i+1}")
        triangle.set_point(create_point(dimensions), i)
        print()

    return triangle


def create_rect(dimensions = 3) -> Rect:
    """
    Создать прямоугольник
    """

    print("Создание фигуры с типом \"Прямоугольник\"\n")
    rect = Rect(dimensions)

    for i in range(4):
        print(f"Точка №{i+1}")
        rect.set_point(create_point(dimensions), i)
        print()

    storony = map(lambda i: Vector(dimensions, rect.points[i], rect.points[(i+1) % 4]), [*range(4)])
    angles = map(lambda i: get_vect_angle(storony[i], storony[(i+1) % 4]), [*range(4)])

    if set(angles) == {90, }: 
        return rect
        
    else: 
        raise Exception("четырёхугольник должен быть прямоугольным выпуклым!")



def create_circle() -> Circle:
    """
    Создать окружность
    """

    print("Создание фигуры с типом \"Окружность\"\n")
    return Circle(create_point(), float(input("Введите радиус окружности >> ")))
