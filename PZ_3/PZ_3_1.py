#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
#лежит во второй или третьей координатной четверти».

#Определяем значение координат
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

#Определяем лежат ли точки или не лежат
if ((x < 0) and (y > 0)) or ((x < 0) and (y < 0)):
    print("Точка с координатами ({}, {}) лежит во второй или третьей координатной четверти.".format(x, y))
else:
    print("Точка с координатами ({}, {}) не лежит во второй или третьей координатной четверти.".format(x, y))