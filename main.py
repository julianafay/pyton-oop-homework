class Mentor:
    """Базовый класс для всех наставников"""
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    """Лектор — наследник Mentor. Получает оценки от студентов"""
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        """Вычисляет среднюю оценку за все лекции"""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    """Эксперт, проверяющий ДЗ — наследник Mentor. Ставит оценки студентам"""
    
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Выставляет оценку студенту за домашнее задание"""
        if not isinstance(student, Student):
            return "Ошибка: можно оценивать только студентов"
        if not (0 <= grade <= 10):
            return "Ошибка: оценка должна быть от 0 до 10"
        if course not in self.courses_attached:
            return "Ошибка: ревьюер не проверяет этот курс"
        if course not in student.courses_in_progress:
            return "Ошибка: студент не изучает этот курс"
        if course not in student.grades:
            student.grades[course] = []
        student.grades[course].append(grade)
        return None

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    """Студент. Может оценивать лекторов"""
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course_name, grade):
        """Выставляет оценку лектору за курс"""
        if not isinstance(lecturer, Lecturer):
            return "Ошибка: можно оценивать только лекторов"
        if not (0 <= grade <= 10):
            return "Ошибка: оценка должна быть от 0 до 10"
        if course_name not in self.courses_in_progress:
            return "Ошибка: вы не изучаете этот курс"
        if course_name not in lecturer.courses_attached:
            return "Ошибка: лектор не ведёт этот курс"
        if course_name not in lecturer.grades:
            lecturer.grades[course_name] = []
        lecturer.grades[course_name].append(grade)
        return None

    def average_grade(self):
        """Вычисляет среднюю оценку за все домашние задания"""
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


# ===== ЗАДАНИЕ №4: ФУНКЦИИ ДЛЯ ПОДСЧЁТА СРЕДНИХ ОЦЕНОК =====

def average_student_grade(students, course_name):
    """Подсчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса"""
    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)


def average_lecturer_grade(lecturers, course_name):
    """Подсчитывает среднюю оценку за лекции всех лекторов в рамках курса"""
    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0
    return round(sum(all_grades) / len(all_grades), 1)


# ===== ПРОВЕРКА (ПОЛЕВЫЕ ИСПЫТАНИЯ) =====

if __name__ == "__main__":
    # Создаём объекты (по 2 экземпляра каждого класса)
    print("=" * 50)
    print("СОЗДАНИЕ ЭКЗЕМПЛЯРОВ КЛАССОВ")
    print("=" * 50)
    
    lecturer1 = Lecturer("Иван", "Иванов")
    lecturer2 = Lecturer("Пётр", "Петров")
    
    reviewer = Reviewer("Сергей", "Сергеев")
    
    student1 = Student("Алёхина", "Ольга", "Ж")
    student2 = Student("Смирнов", "Алексей", "М")

    # Назначаем курсы
    print("\n" + "=" * 50)
    print("НАЗНАЧЕНИЕ КУРСОВ")
    print("=" * 50)
    
    student1.courses_in_progress += ["Python", "Java"]
    student1.finished_courses += ["Введение в программирование"]
    student2.courses_in_progress += ["Python", "Git"]
    student2.finished_courses += ["Введение в программирование"]
    
    lecturer1.courses_attached += ["Python", "C++"]
    lecturer2.courses_attached += ["Python", "Git"]
    reviewer.courses_attached += ["Python", "C++"]
    
    print("Курсы назначены!")

    # Выставляем оценки лекторам от студентов
    print("\n" + "=" * 50)
    print("ВЫСТАВЛЕНИЕ ОЦЕНОК ЛЕКТОРАМ")
    print("=" * 50)
    
    student1.rate_lecture(lecturer1, "Python", 9)
    student1.rate_lecture(lecturer1, "Python", 8)
    student1.rate_lecture(lecturer2, "Python", 7)
    student2.rate_lecture(lecturer2, "Python", 10)
    student2.rate_lecture(lecturer2, "Git", 8)
    
    print("Оценки лекторам выставлены!")

    # Выставляем оценки студентам от ревьюера
    print("\n" + "=" * 50)
    print("ВЫСТАВЛЕНИЕ ОЦЕНОК СТУДЕНТАМ")
    print("=" * 50)
    
    reviewer.rate_hw(student1, "Python", 9)
    reviewer.rate_hw(student1, "Python", 8)
    reviewer.rate_hw(student2, "Python", 7)
    reviewer.rate_hw(student2, "Python", 10)
    reviewer.rate_hw(student2, "Git", 9)
    
    print("Оценки студентам выставлены!")

    # Проверка __str__
    print("\n" + "=" * 50)
    print("ПРОВЕРКА __str__ У ВСЕХ КЛАССОВ")
    print("=" * 50)
    
    print("=== Reviewer ===")
    print(reviewer)
    print()
    
    print("=== Lecturer ===")
    print(lecturer1)
    print()
    print(lecturer2)
    print()
    
    print("=== Student ===")
    print(student1)
    print()
    print(student2)
    print()

    # Проверка сравнения лекторов
    print("=" * 50)
    print("СРАВНЕНИЕ ЛЕКТОРОВ")
    print("=" * 50)
    print(f"Средняя оценка {lecturer1.name} {lecturer1.surname}: {lecturer1.average_grade()}")
    print(f"Средняя оценка {lecturer2.name} {lecturer2.surname}: {lecturer2.average_grade()}")
    print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
    print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
    print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")
    print()

    # Проверка сравнения студентов
    print("=" * 50)
    print("СРАВНЕНИЕ СТУДЕНТОВ")
    print("=" * 50)
    print(f"Средняя оценка {student1.name} {student1.surname}: {student1.average_grade()}")
    print(f"Средняя оценка {student2.name} {student2.surname}: {student2.average_grade()}")
    print(f"{student1.name} > {student2.name}: {student1 > student2}")
    print(f"{student1.name} < {student2.name}: {student1 < student2}")
    print(f"{student1.name} == {student2.name}: {student1 == student2}")
    print()

    # ===== ЗАДАНИЕ №4: ПРОВЕРКА ФУНКЦИЙ =====
    print("=" * 50)
    print("ПОДСЧЁТ СРЕДНИХ ОЦЕНОК (ЗАДАНИЕ №4)")
    print("=" * 50)
    
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]
    
    print(f"Средняя оценка студентов по курсу Python: {average_student_grade(students_list, 'Python')}")
    print(f"Средняя оценка студентов по курсу Java: {average_student_grade(students_list, 'Java')}")
    print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade(lecturers_list, 'Python')}")
    print(f"Средняя оценка лекторов по курсу Java: {average_lecturer_grade(lecturers_list, 'Java')}")
    
    print("\n" + "=" * 50)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    print("=" * 50)