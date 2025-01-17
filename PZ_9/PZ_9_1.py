# Создаем списоск с фрутками
dictionary = {
    "apple": "яблоко",
    "banana": "банан",
    "orange": "апельсин",
    "strawberry": "клубника",
    "lemone": "лимон",
    "peach": "персик",
    "kiwi": "киви",
    "cherry": "вишня",
    "grape": "виноград",
    "tangerine": "мандарин",
}



# Функция для перевода c английского на русккий
def translate(word):
    return dictionary.get(word.lower(), "Слово не найдено")

# Определяем как основную и выводим результат
if __name__ == "__main__":
    english_word = input("Введите английское слово для перевода: ")
    russian_translation = translate(english_word)
    print(f"Перевод: {russian_translation}")
