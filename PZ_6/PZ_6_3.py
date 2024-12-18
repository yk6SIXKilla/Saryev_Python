#Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти
#наибольший периметр треугольника, вершины которого принадлежат различным
#точкам множества A, и сами эти точки (точки выводятся в том же порядке, в котором
#они перечислены при задании множества A).
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2
#Для хранения данных о каждом наборе точек следует использовать по два список: первый
#список для хранения абсцисс, второй — для хранения ординат.


import math

def max_triangle_perimeter(x_coords, y_coords):
    n = len(x_coords)
    max_perimeter = 0
    best_triangle = None

    # Перебор всех троек точек
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Вычисление длин сторон треугольника
                a = math.sqrt((x_coords[i] - x_coords[j])**2 + (y_coords[i] - y_coords[j])**2)
                b = math.sqrt((x_coords[i] - x_coords[k])**2 + (y_coords[i] - y_coords[k])**2)
                c = math.sqrt((x_coords[j] - x_coords[k])**2 + (y_coords[j] - y_coords[k])**2)

                # Проверка существования треугольника
                if a + b > c and a + c > b and b + c > a:
                    perimeter = a + b + c
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        best_triangle = (i, j, k)

    if best_triangle is not None:
        print("Максимальный периметр:", max_perimeter)
        print("Координаты вершин треугольника:")
        print(f"Точка 1: ({x_coords[best_triangle[0]]}, {y_coords[best_triangle[0]]})")
        print(f"Точка 2: ({x_coords[best_triangle[1]]}, {y_coords[best_triangle[1]]})")
        print(f"Точка 3: ({x_coords[best_triangle[2]]}, {y_coords[best_triangle[2]]})")
    else:
        print("Не удалось найти треугольник.")

# Пример использования
x_coordinates = [0, 3, 6, 2]
y_coordinates = [0, 4, 1, 5]
max_triangle_perimeter(x_coordinates, y_coordinates)