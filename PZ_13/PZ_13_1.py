# В двумерном списке найти среднее арифметическое положительных элементов,
# кратных 3.


def average_positive_multiples_of_three(matrix):
    total = 0
    count = 0
    for row in matrix:
        for element in row:
            if element > 0 and element % 3 == 0:
                total += element
                count += 1
    if count == 0:
        return None  # или можно вернуть 0, если подходящих элементов нет
    return total / count

# Пример использования:
matrix = [
    [3, -6, 9],
    [12, 5, 7],
    [-3, 0, 15]
]

result = average_positive_multiples_of_three(matrix)
if result is not None:
    print(f"Среднее арифметическое положительных элементов, кратных 3: {result}")
else:
    print("Подходящих элементов не найдено.")