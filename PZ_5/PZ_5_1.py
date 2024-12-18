import random


def generate_four_digit_number():
    # Генерируем случайное четырехзначное число
    number = random.randint(1000, 9999)
    return number


def has_duplicate_digits(number):
    # Преобразуем число в строку и создаем множество для проверки уникальности цифр
    digits = str(number)
    unique_digits = set(digits)

    # Если длина множества меньше длины строки, значит есть повторяющиеся цифры
    return len(unique_digits) < len(digits)


def main():
    # Генерируем число
    number = generate_four_digit_number()
    print(f"Сгенерированное четырехзначное число: {number}")

    # Проверяем на наличие одинаковых цифр
    if has_duplicate_digits(number):
        print("В числе есть одинаковые цифры.")
    else:
        print("В числе нет одинаковых цифр.")


# Запускаем основную функцию
if __name__ == "__main__":
    main()