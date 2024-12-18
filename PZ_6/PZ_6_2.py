#Дан целочисленный список A размера N. Переписать в новый целочисленный
#список B все четные числа из исходного списка (в том же порядке) и вывести размер
#полученного список B и его содержимое.


def extract_even_numbers(A):
    B = []  # Инициализируем пустой список для четных чисел
    for number in A:  # Проходим по каждому элементу в списке A
        if number % 2 == 0:  # Проверяем, является ли число четным
            B.append(number)  # Добавляем четное число в список B

    return B  # Возвращаем новый список с четными числами


# Пример использования
A = [5, 3, 8, 1, 4, 7, 10, 12]
B = extract_even_numbers(A)

# Выводим размер и содержимое списка B
print("Размер списка B:", len(B))
print("Содержимое списка B:", B)