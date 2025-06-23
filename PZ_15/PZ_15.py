import sqlite3

# Создание базы данных и таблицы, если их нет
def init_db():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buyer TEXT NOT NULL,
            product TEXT NOT NULL,
            unit TEXT NOT NULL,
            quantity REAL NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Добавление новой продажи
def add_sale():
    buyer = input("ФИО покупателя: ")
    product = input("Товар: ")
    unit = input("Единица измерения (штуки, килограммы, литры): ")
    quantity = float(input("Количество: "))
    price = float(input("Стоимость: "))

    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO sales (buyer, product, unit, quantity, price)
        VALUES (?, ?, ?, ?, ?)
    ''', (buyer, product, unit, quantity, price))
    conn.commit()
    conn.close()
    print("Продажа успешно добавлена!\n")

# Просмотр всех продаж
def view_sales():
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute('SELECT buyer, product, unit, quantity, price FROM sales')
    sales = c.fetchall()
    conn.close()

    print("\nСписок продаж:")
    for sale in sales:
        print(f"Покупатель: {sale[0]}, Товар: {sale[1]}, Ед. изм.: {sale[2]}, Кол-во: {sale[3]}, Стоимость: {sale[4]}")
    print()

# Главное меню
def main():
    init_db()
    while True:
        print("1. Добавить продажу")
        print("2. Просмотреть все продажи")
        print("3. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            add_sale()
        elif choice == '2':
            view_sales()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.\n")

if __name__ == '__main__':
    main()
