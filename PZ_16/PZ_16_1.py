#Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником.


class Student:
    def __init__(self, first_name, last_name, grades):
        """
        Инициализация студента.

        :param first_name: Имя студента (строка)
        :param last_name: Фамилия студента (строка)
        :param grades: Список оценок (список чисел)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        """
        Вычисляет средний балл студента.

        :return: Средний балл (float), 0 если оценок нет
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_honor_student(self):
        """
        Определяет, является ли студент отличником.
        Предположим, что отличник — это студент со средним баллом >= 4.5.

        :return: True если отличник, иначе False
        """
        return self.average_grade() >= 4.5

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Средний балл: {self.average_grade():.2f}, Отличник: {'Да' if self.is_honor_student() else 'Нет'}"


# Пример использования:
student1 = Student("Иван", "Иванов", [5, 4, 5, 5, 4])
student2 = Student("Мария", "Петрова", [3, 4, 3, 4, 3])

print(student1)
print(student2)