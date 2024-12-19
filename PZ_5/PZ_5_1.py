# Составить программу, в которо функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры


import random


def generate_four_digit_number():
    # Генерируем случайное четырехзначное число
    number = random.randint(1000, 9999)
    return number


def has_duplicate_digits(number):
    # Создаем множество для хранения уникальных цифр
    unique_digits = set()

    while number > 0:
        digit = number % 10  # Извлекаем последнюю цифру
        if digit in unique_digits:
            return True  # Если цифра уже есть в множестве, значит есть дубликаты
        unique_digits.add(digit)  # Добавляем цифру в множество
        number //= 10  # Удаляем последнюю цифру из числа

    return False  # Если дубликатов нет


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