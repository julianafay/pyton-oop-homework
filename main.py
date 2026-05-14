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

    # Методы сравнения лекторов по средней оценке
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

    # Методы сравнения студентов по средней оценке
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


if __name__ == "__main__":
    # Создаём объекты
    lecturer1 = Lecturer("Иван", "Иванов")
    lecturer2 = Lecturer("Пётр", "Петров")
    reviewer = Reviewer("Сергей", "Сергеев")
    student1 = Student("Алёхина", "Ольга", "Ж")
    student2 = Student("Смирнов", "Алексей", "М")

    # Назначаем курсы
    student1.courses_in_progress += ["Python", "Java"]
    student1.finished_courses += ["Введение в программирование"]
    student2.courses_in_progress += ["Python", "Git"]
    student2.finished_courses += ["Введение в программирование"]
    
    lecturer1.courses_attached += ["Python", "C++"]
    lecturer2.courses_attached += ["Python", "Git"]
    reviewer.courses_attached += ["Python", "C++"]

    # Выставляем оценки лекторам от студентов
    student1.rate_lecture(lecturer1, "Python", 9)
    student1.rate_lecture(lecturer1, "Python", 8)
    student1.rate_lecture(lecturer2, "Python", 7)
    student2.rate_lecture(lecturer2, "Python", 10)
    student2.rate_lecture(lecturer2, "Git", 8)

    # Выставляем оценки студентам от ревьюера
    reviewer.rate_hw(student1, "Python", 9)
    reviewer.rate_hw(student1, "Python", 8)
    reviewer.rate_hw(student2, "Python", 7)
    reviewer.rate_hw(student2, "Python", 10)
    reviewer.rate_hw(student2, "Git", 9)

    # Проверка __str__
    print("=== Проверка __str__ у Reviewer ===")
    print(reviewer)
    print()

    print("=== Проверка __str__ у Lecturer ===")
    print(lecturer1)
    print()
    print(lecturer2)
    print()

    print("=== Проверка __str__ у Student ===")
    print(student1)
    print()
    print(student2)
    print()

    # Проверка сравнения лекторов
    print("=== Сравнение лекторов ===")
    print(f"Средняя оценка {lecturer1.name} {lecturer1.surname}: {lecturer1.average_grade()}")
    print(f"Средняя оценка {lecturer2.name} {lecturer2.surname}: {lecturer2.average_grade()}")
    print(f"{lecturer1.name} > {lecturer2.name}: {lecturer1 > lecturer2}")
    print(f"{lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}")
    print(f"{lecturer1.name} == {lecturer2.name}: {lecturer1 == lecturer2}")
    print()

    # Проверка сравнения студентов
    print("=== Сравнение студентов ===")
    print(f"Средняя оценка {student1.name} {student1.surname}: {student1.average_grade()}")
    print(f"Средняя оценка {student2.name} {student2.surname}: {student2.average_grade()}")
    print(f"{student1.name} > {student2.name}: {student1 > student2}")
    print(f"{student1.name} < {student2.name}: {student1 < student2}")
    print(f"{student1.name} == {student2.name}: {student1 == student2}")