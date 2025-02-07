def count_words(input_string):
    words = input_string.split()  # Раздляет строку на список слов по пробелам
    word_count = len(words)  # Подсчитывает количество элементов в списке
    return word_count


string = "Я   люблю   РКСИ  "
count = count_words(string)
print(f"Количество слов: {count}")
