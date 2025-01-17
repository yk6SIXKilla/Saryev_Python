dictionary = {
    "apple": "яблоко",
    "banana": "банан",
    "orange": "апельсин",
    "strawberry": "клубника",
    "lemone": "лимон",
    "peach": "персик",
    "kiwi": "киви",
    "cherry": "вишня",
}


# Функция для перевода
def translate(word):
    return dictionary.get(word.lower(), "Слово не найдено")


if __name__ == "__main__":
    english_word = input("Введите английское слово для перевода: ")
    russian_translation = translate(english_word)
    print(f"Перевод: {russian_translation}")
