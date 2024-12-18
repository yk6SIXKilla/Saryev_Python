#Дан список A размера N. Найти минимальный элемент из его элементов с четными
#номерами: A2, A4, A6, ...

def find_min_even_indexed(A):
    if len(A) < 2:
        return None  # Если нет четных индексов

    min_value = float('inf')  # Инициализируем минимальное значение
    for i in range(1, len(A), 2):  # Проходим по четным индексам (A[2], A[4], ...)
        if A[i] < min_value:
            min_value = A[i]

    return min_value if min_value != float('inf') else None


# Пример использования
A = [5, 3, 8, 1, 4, 7]
min_even_indexed = find_min_even_indexed(A)
print("Минимальный элемент с четными индексами:", min_even_indexed)