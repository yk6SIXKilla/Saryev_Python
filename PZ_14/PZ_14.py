#Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
#год и поместить ее в новый текстовый файл.


import re

# Открываем исходный файл для чтения
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Регулярное выражение для поиска блока за 1857 год
pattern = r'1857 год\s*(.*?)(?=\d{4} год|\d{4}–\d{4} гг\.|Последние годы жизни|$)'

# Ищем нужный блок
match = re.search(pattern, text, re.DOTALL)

if match:
    block_1857 = match.group(0).strip()
    # Записываем найденный блок в новый файл
    with open('Dostoevsky_1857.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(block_1857)
    print('Блок за 1857 год успешно сохранён в Dostoevsky_1857.txt')
else:
    print('Блок за 1857 год не найден.')