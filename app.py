# Лабораторная работа по ООП № 2
# Выполнил Прокофьев Андрей Фт-210008

from objects.figures import (
    Point, Rectangular, Round, Triangle, Vector, get_vect_angle
)


def create_triangle() -> Triangle:
    """
    Создать треугольник
    """

    print("Создание фигуры с типом \"Треугольник\"\n")
    triangle = Triangle()

    for i in range(3):
        print(f"Точка №{i+1}")
        x = int(input("Введите x для точки >> "))
        y = int(input("Введите y для точки >> "))
        z = int(input("Введите z для точки >> "))

        triangle.set_point(Point(x,y,z), i)

    return triangle


def create_rect() -> Rectangular:
    """
    Создать прямоугольник
    """

    print("Создание фигуры с типом \"Прямоугольник\"\n")
    rect = Rectangular()

    for i in range(4):
        print(f"Точка №{i+1}")
        x = int(input("Введите x для точки >> "))
        y = int(input("Введите y для точки >> "))
        z = int(input("Введите z для точки >> "))

        rect.set_point(Point(x,y,z), i)
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

    x = int(input("Введите x для точки >> "))
    y = int(input("Введите y для точки >> "))
    z = int(input("Введите z для точки >> "))

    r = int(input("Введите радиус окружности >> "))
    
    round_figure = Round()
    round_figure.set_pos(Point(x, y, z))
    round_figure.radius = r

    return round_figure


def main() -> None:
    """
    Главная функция
    """

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
    print("Список отсортирован по показателям площади")

    print("Список фигур: ")
    for i in figure_list:
        print(i.output())
    return


# Запуск через "python3 app.py"
if __name__ == "__main__":
    main()