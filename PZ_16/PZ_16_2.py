class Avtomobil:
    def __init__(self, marka, model, god_vypuska):
        self.marka = marka
        self.model = model
        self.god_vypuska = god_vypuska

    def info(self):
        return f"Марка: {self.marka}, Модель: {self.model}, Год выпуска: {self.god_vypuska}"

# Класс Грузовик, наследуется от Автомобиль
class Gruzovik(Avtomobil):
    def __init__(self, marka, model, god_vypuska, gruzopodemnost):
        super().__init__(marka, model, god_vypuska)
        self.gruzopodemnost = gruzopodemnost  # в килограммах

    def info(self):
        base_info = super().info()
        return f"{base_info}, Грузоподъемность: {self.gruzopodemnost} кг"

# Класс Легковой автомобиль, наследуется от Автомобиль
class LegkovoyAvtomobil(Avtomobil):
    def __init__(self, marka, model, god_vypuska, kolichestvo_passazhirov):
        super().__init__(marka, model, god_vypuska)
        self.kolichestvo_passazhirov = kolichestvo_passazhirov

    def info(self):
        base_info = super().info()
        return f"{base_info}, Количество пассажиров: {self.kolichestvo_passazhirov}"

# Пример использования
if __name__ == "__main__":
    gruzovik = Gruzovik("КАМАЗ", "65115", 2015, 10000)
    legkovoy = LegkovoyAvtomobil("Toyota", "Camry", 2020, 5)

    print(gruzovik.info())
    print(legkovoy.info())