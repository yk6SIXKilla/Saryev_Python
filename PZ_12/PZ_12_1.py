# В последовательности их N чисел (N –четное) в первой ее половине найти
# произведение элементов меньших 0.


def product_of_negatives_in_first_half(sequence):
    n = len(sequence)
    if n % 2 != 0:
        return "Длина последовательности должна быть четной"
    first_half = sequence[:n//2]
    product = 1
    found_negative = False
    for num in first_half:
        if num < 0:
            product *= num
            found_negative = True
    if not found_negative:
        return 0  # Если отрицательных чисел нет, возвращаем 0
    return product

# Пример использования:
example_sequence = [1, -2, 3, -4, 5, 6]
result = product_of_negatives_in_first_half(example_sequence)
print(result)