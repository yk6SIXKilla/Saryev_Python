import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Выбрать из справочника")
root.geometry("570x520")
root.configure(bg="white")
root.resizable(False, False)

# Ссылка сверху
link = tk.Label(
    root,
    text="выбрать из справочника",
    fg="#1a92d2",
    cursor="hand2",
    bg="white",
    font=("Arial", 16, "underline")
)
link.place(x=18, y=12)

# Основная рамка
main_frame = tk.Frame(root, bg="#ededed", bd=1, relief="solid")
main_frame.place(x=15, y=45, width=540, height=430)

# Заголовки
labels = [
    ("Регион", 30, 30),
    ("Район", 30, 90),
    ("Город", 30, 150),
    ("Улица", 30, 210),
    ("Дом", 30, 270),
    ("Корпус", 210, 270),
    ("Стр./Вл.", 30, 330),
    ("Кв./Офис", 210, 330)
]
for text, x, y in labels:
    font = ("Arial", 14, "bold") if y < 270 else ("Arial", 13)
    tk.Label(main_frame, text=text, bg="#ededed", font=font, anchor="w").place(x=x, y=y)

# Combobox style
style = ttk.Style()
style.theme_use('default')
style.configure(
    "TCombobox",
    fieldbackground="#f9f9f9",
    background="#f9f9f9",
    bordercolor="#d9d9d9",
    relief="flat",
    padding=8,
    font=("Arial", 15)
)

# Combobox'ы
region_cb = ttk.Combobox(main_frame, values=["[ не выбрано ]"], state="readonly", font=("Arial", 15))
region_cb.current(0)
region_cb.place(x=30, y=55, width=480, height=35)

district_cb = ttk.Combobox(main_frame, values=["Выберите район"], state="readonly", font=("Arial", 15))
district_cb.current(0)
district_cb.place(x=30, y=115, width=480, height=35)

city_cb = ttk.Combobox(main_frame, values=["Выберите город"], state="readonly", font=("Arial", 15))
city_cb.current(0)
city_cb.place(x=30, y=175, width=480, height=35)

street_cb = ttk.Combobox(main_frame, values=["Выберите улицу"], state="readonly", font=("Arial", 15))
street_cb.current(0)
street_cb.place(x=30, y=235, width=480, height=35)

# Entry поля
entry_style = {
    "font": ("Arial", 15),
    "bg": "white",
    "relief": "flat",
    "highlightbackground": "#d9d9d9",
    "highlightcolor": "#1a92d2",
    "highlightthickness": 1
}
house_entry = tk.Entry(main_frame, **entry_style)
house_entry.place(x=30, y=295, width=150, height=35)

building_entry = tk.Entry(main_frame, **entry_style)
building_entry.place(x=210, y=295, width=150, height=35)

str_entry = tk.Entry(main_frame, **entry_style)
str_entry.place(x=30, y=355, width=150, height=35)

apt_entry = tk.Entry(main_frame, **entry_style)
apt_entry.place(x=210, y=355, width=150, height=35)

# Кнопки
def on_enter(e):
    e.widget['bg'] = "#e0e0e0"
def on_leave(e):
    e.widget['bg'] = "#f5f5f5"

ok_btn = tk.Button(
    main_frame, text="OK",
    font=("Arial", 18, "bold"),
    fg="#1a92d2",
    bg="#f5f5f5",
    bd=0,
    activebackground="#e0e0e0",
    cursor="hand2"
)
ok_btn.place(x=60, y=385, width=180, height=50)
ok_btn.bind("<Enter>", on_enter)
ok_btn.bind("<Leave>", on_leave)

cancel_btn = tk.Button(
    main_frame, text="ОТМЕНА",
    font=("Arial", 18, "bold"),
    fg="#1a92d2",
    bg="#f5f5f5",
    bd=0,
    activebackground="#e0e0e0",
    cursor="hand2"
)
cancel_btn.place(x=300, y=385, width=180, height=50)
cancel_btn.bind("<Enter>", on_enter)
cancel_btn.bind("<Leave>", on_leave)

root.mainloop()