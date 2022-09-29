# Лабораторная работа по ООП № 2
# Выполнил Прокофьев Андрей Фт-210008


import argparse
from math import acos, pi
from objects.figures import (
    Point, Rectangular, Round, Triangle, Vector, DIMENSIONS
)


def create_point():
    return Point(*[float(input(f"Введите точку в измерении {j} >> ")) for j in range(DIMENSIONS)])


def create_vector():
    return Vector(create_point(), create_point())


def create_triangle() -> Triangle:
    """
    Создать треугольник
    """

    print("Создание фигуры с типом \"Треугольник\"\n")
    triangle = Triangle()

    for i in range(3):
        print(f"Точка №{i+1}")
        # x = int(input("Введите x для точки >> "))
        # y = int(input("Введите y для точки >> "))
        # z = int(input("Введите z для точки >> "))

        # triangle.set_point(Point(x,y,z), i)

        triangle.set_point(create_point(), i)


    return triangle


def create_rect() -> Rectangular:
    """
    Создать прямоугольник
    """

    print("Создание фигуры с типом \"Прямоугольник\"\n")
    rect = Rectangular()

    for i in range(4):
        print(f"Точка №{i+1}")
        rect.set_point(create_point(), i)
        print()

    a = "четырёхугольник должен быть прямоугольным выпуклым!"
    A = rect.points[0]
    B = rect.points[1]
    C = rect.points[2]
    D = rect.points[3]

    AB = Vector(A, B)
    BC = Vector(B, C)
    CD = Vector(C, D)
    DA = Vector(D, A)
    e = get_vect_angle(AB, BC)
    ee = get_vect_angle(BC, CD)
    eee = get_vect_angle(CD, DA)
    eeee = get_vect_angle(AB, DA)
    if e != 90:
        raise Exception(a + f"; {e=}")

    if ee != 90:
        raise Exception(a + f"; {ee=}")
    
    if eee != 90:
        raise Exception(a + f"; {eee=}")

    if eeee != 90:
        raise Exception(a + f"; {eeee=}")

    return rect


def create_round() -> Round:
    """
    Создать окружность
    """

    print("Создание фигуры с типом \"Окружность\"\n")

    round_figure = Round()
    round_figure.set_pos(create_point())
    round_figure.radius = int(input("Введите радиус окружности >> "))

    return round_figure


def get_vect_angle(v1: Vector, v2: Vector):
    # poss = v1.get_proj("x") * v2.get_proj("x") + v1.get_proj("y") * v2.get_proj("y") + v1.get_proj("z") * v2.get_proj("z")
    poss = sum(map(lambda x: v1.get_proj(x) * v2.get_proj(x), [*range(DIMENSIONS)]))
    lens = abs(v1) * abs(v2)
    angle = poss / lens 

    return acos(angle) / pi * 90 * 2 // 0.0000001 / 10000000


def main() -> None:
    """
    Главная функция
    """
    parser = argparse.ArgumentParser(description='Парсер.')
    parser.add_argument('-o', '--output', type=str, help="Куда отправлять результат")
    args = parser.parse_args()

    print("Создание списка фигур")
    print()

    figure_count = int(input("Сколько фигур нужно в списке? >> "))
    figure_list = []
    print()

    print("Для каждой фигуры нужно определить свой тип. Даны следующие типы:\n\t0 - Треугольник\n\t1 - Прямоугольник\n\t2 - Круг")
    print()

    for i in range(figure_count):
        print(f"Фигура №{i+1}")
        cycle = True

        while cycle:
            figure_type = input("Введите индекс типа фигуры >> ").lower()

            if figure_type in ["0", "треугольник"]:
                figure = create_triangle()

            elif figure_type in ["1", "прямоугольник"]:
                try:
                    figure = create_rect()
                    
                except Exception as e:
                    print(e)

                    continue

            elif figure_type in ["2", "окружность"]:
                figure = create_round()

            else:
                print("Такого типа фигуры не существует! Попробуйте ещё раз!")
                continue

            figure_list.append(figure)
            cycle = False
        
        print("Фигура создана и занесена в список.")
        print()
        
    figure_list = sorted(figure_list, key = lambda s: s.get_area())
    response = "Список отсортирован по показателям площади\nСписок фигур: \n"

    for i in figure_list:
        response += "\t" + i.output() + "\n"

    if args.output:
        with open(args.output, "w+", encoding="utf-8") as file:
            file.write(response)
            print("Ваш результат записан в указанном файле:", args.output)

    else:
        print("Ваш результат:", response)

    return


# Запуск через "python3 app.py"
if __name__ == "__main__":
    main()