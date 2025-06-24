import pickle


class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_honor_student(self):
        return self.average_grade() >= 4.5

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Средний балл: {self.average_grade():.2f}, Отличник: {'Да' if self.is_honor_student() else 'Нет'}"


def save_def(students, filename):
    """
    Сохраняет список объектов Student в файл с помощью pickle.

    :param students: список из 3 объектов Student
    :param filename: имя файла для сохранения (строка)
    """
    with open(filename, 'wb') as file:
        pickle.dump(students, file)
    print(f"Данные успешно сохранены в файл '{filename}'.")


def load_def(filename):
    """
    Загружает список объектов Student из файла с помощью pickle.

    :param filename: имя файла для загрузки (строка)
    :return: список объектов Student
    """
    with open(filename, 'rb') as file:
        students = pickle.load(file)
    print(f"Данные успешно загружены из файла '{filename}'.")
    return students


# Пример использования:

# Создаём 3 объекта Student
student1 = Student("Иван", "Иванов", [5, 4, 5, 5, 4])
student2 = Student("Мария", "Петрова", [3, 4, 3, 4, 3])
student3 = Student("Алексей", "Сидоров", [5, 5, 5, 4, 5])

students_list = [student1, student2, student3]

# Сохраняем список студентов в файл
save_def(students_list, "students_data.pkl")

# Загружаем список студентов из файла
loaded_students = load_def("students_data.pkl")

# Выводим загруженных студентов
for student in loaded_students:
    print(student)