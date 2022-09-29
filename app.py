# Лабораторная работа по ООП № 2
# Выполнил Прокофьев Андрей Фт-210008


import argparse
from tools import create_circle, create_rect, create_triangle


def main() -> None:
    """
    Главная функция
    """
    figure_list = []
    parser = argparse.ArgumentParser(description='Парсер.')
    parser.add_argument('-o', '--output', type=str, help="Куда отправлять результат")
    parser.add_argument('-d', '--dimensions', type=int, help="Количество измерений пространств")
    parser.add_argument('-c', '--count', type=int, help="Количество фигур в списке")
    args = parser.parse_args()

    print("Создание списка фигур")
    print()
    figure_count = args.count or int(input("Сколько фигур нужно в списке? >> "))
    print()

    for i in range(figure_count):
        print(f"Фигура №{i+1}")
        cycle = True

        while cycle:
            figure_type = input("Введите тип фигуры >> ").lower()

            if figure_type in ["0", "треугольник"]:
                figure = create_triangle(args.dimensions)

            elif figure_type in ["1", "прямоугольник", "квадрат"]:
                try:
                    figure = create_rect(args.dimensions)
                    
                except Exception as e:
                    print(e)

                    continue

            elif figure_type in ["2", "окружность", "круг"]:
                figure = create_circle(args.dimensions)

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