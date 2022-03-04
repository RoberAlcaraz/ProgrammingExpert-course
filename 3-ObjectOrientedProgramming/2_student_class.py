class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if not 0 <= grade <= 100:
            raise ValueError()
        self._grade = grade

    def calculate_average_grade(students):
        if students == []:
            return -1

        grades_of_students = []
        for student in students:
            grades_of_students.append(student.grade)

        return sum(grades_of_students) / len(grades_of_students)

    @classmethod
    def get_average_grade(cls):

        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        if cls.all_students == []:
            return None

        best_grade = 0
        best_student = ''
        for student in cls.all_students:
            if student.grade > best_grade:
                best_student = student
                best_grade = student.grade

        return best_student


students = [
    Student("Simon", 55),
    Student("Alex", 69),
    Student("James", 8),
]
best_student = Student.calculate_average_grade(students)
print(best_student)
