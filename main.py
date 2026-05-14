class Mentor:
    """Базовый класс для всех наставников"""
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Лектор — наследник Mentor. Получает оценки от студентов"""
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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


if __name__ == "__main__":
    # Создаём объекты
    lecturer = Lecturer("Иван", "Иванов")
    reviewer = Reviewer("Пётр", "Петров")
    student = Student("Алёхина", "Ольга", "Ж")

    # Назначаем курсы
    student.courses_in_progress += ["Python", "Java"]
    lecturer.courses_attached += ["Python", "C++"]
    reviewer.courses_attached += ["Python", "C++"]

    # Проверка rate_lecture
    print("=== Проверка rate_lecture ===")
    print(student.rate_lecture(lecturer, "Python", 7))
    print(student.rate_lecture(lecturer, "Java", 8))
    print(student.rate_lecture(lecturer, "C++", 8))
    print(student.rate_lecture(reviewer, "Python", 6))

    # Вывод оценок лектора
    print("\n=== Оценки лектора ===")
    print(lecturer.grades)

    # Проверка rate_hw
    print("\n=== Проверка rate_hw ===")
    reviewer.rate_hw(student, "Python", 9)
    print(student.grades)