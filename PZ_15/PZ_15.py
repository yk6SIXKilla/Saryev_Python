# приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
# содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
# единицу измерения (штуки, килограммы, литры), количество, стоимость.


import sqlite3

# Создаем (или подключаемся к) файл базы данных
conn = sqlite3.connect('internet_shop.dat')
cursor = conn.cursor()

# Создаем таблицу продаж, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    product TEXT NOT NULL,
    unit TEXT CHECK(unit IN ('штуки', 'килограммы', 'литры')) NOT NULL,
    quantity REAL NOT NULL,
    price REAL NOT NULL
)
''')

# Заполняем таблицу 10 записями (пример)
sales_data = [
    ('Иванов Иван Иванович', 'Молоко', 'литры', 2, 60),
    ('Петров Петр Петрович', 'Яблоки', 'килограммы', 1.5, 90),
    ('Сидоров Сидор Сидорович', 'Хлеб', 'штуки', 3, 75),
    ('Кузнецова Анна', 'Масло', 'килограммы', 0.5, 150),
    ('Васильев Василий', 'Сок', 'литры', 1, 80),
    ('Морозова Мария', 'Яйца', 'штуки', 10, 120),
    ('Новиков Николай', 'Картофель', 'килограммы', 5, 100),
    ('Федорова Ольга', 'Сахар', 'килограммы', 2, 70),
    ('Смирнов Алексей', 'Чай', 'штуки', 4, 200),
    ('Егоров Евгений', 'Кофе', 'килограммы', 1, 500)
]

# Вставляем данные, если таблица пустая
cursor.execute('SELECT COUNT(*) FROM sales')
if cursor.fetchone()[0] == 0:
    cursor.executemany('INSERT INTO sales (customer_name, product, unit, quantity, price) VALUES (?, ?, ?, ?, ?)', sales_data)
    conn.commit()

# Функция для управления программой через консоль
def menu():
    while True:
        print("\nМеню управления интернет-магазином:")
        print("1. Показать все продажи")
        print("2. Добавить продажу")
        print("3. Удалить продажу по ID")
        print("4. Обновить данные продажи по ID")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            cursor.execute('SELECT * FROM sales')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        elif choice == '2':
            customer_name = input("ФИО покупателя: ")
            product = input("Товар: ")
            unit = input("Единица измерения (штуки, килограммы, литры): ")
            quantity = float(input("Количество: "))
            price = float(input("Стоимость: "))
            cursor.execute('INSERT INTO sales (customer_name, product, unit, quantity, price) VALUES (?, ?, ?, ?, ?)',
                           (customer_name, product, unit, quantity, price))
            conn.commit()
            print("Продажа добавлена.")
        elif choice == '3':
            sale_id = int(input("Введите ID продажи для удаления: "))
            cursor.execute('DELETE FROM sales WHERE id = ?', (sale_id,))
            conn.commit()
            print("Продажа удалена.")
        elif choice == '4':
            sale_id = int(input("Введите ID продажи для обновления: "))
            customer_name = input("Новое ФИО покупателя: ")
            product = input("Новый товар: ")
            unit = input("Новая единица измерения (штуки, килограммы, литры): ")
            quantity = float(input("Новое количество: "))
            price = float(input("Новая стоимость: "))
            cursor.execute('''
                UPDATE sales SET customer_name = ?, product = ?, unit = ?, quantity = ?, price = ?
                WHERE id = ?
            ''', (customer_name, product, unit, quantity, price, sale_id))
            conn.commit()
            print("Данные продажи обновлены.")
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

menu()

# Закрываем соединение с базой данных
conn.close()