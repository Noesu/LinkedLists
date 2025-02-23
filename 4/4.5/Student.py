class Student:
    def __init__(self, fio: str, group: str) -> None:
        self._fio = fio
        self._group = group
        self._lect_marks: list = []  # оценки за лекции
        self._house_marks: list = []  # оценки за домашние задания

    def add_lect_marks(self, mark: int) -> None:
        self._lect_marks.append(mark)

    def add_house_marks(self, mark: int) -> None:
        self._house_marks.append(mark)

    def __str__(self) -> str:
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    def __init__(self, fio: str, subject: str) -> None:
        self._fio = fio
        self._subject = subject

# здесь продолжайте программу

class Lector(Mentor):
    def __str__(self) -> str:
        return f'Лектор {self._fio}: предмет {self._subject}'

    def set_mark(self, student: Student, mark: int):
        student.add_lect_marks(mark)

class Reviewer(Mentor):
    def __str__(self) -> str:
        return f'Эксперт {self._fio}: предмет {self._subject}'

    def set_mark(self, student: Student, mark: int):
        student.add_house_marks(mark)




########################################################################################################################

lector = Lector("Балакирев С.М.", "Информатика")
reviewer = Reviewer("Гейтс Б.", "Информатика")
students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
persons = [lector, reviewer]
lector.set_mark(students[0], 4)
lector.set_mark(students[1], 2)
reviewer.set_mark(students[0], 5)
reviewer.set_mark(students[1], 3)
for p in persons + students:
    print(p)
# в консоли будет отображено:
# Лектор Балакирев С.М.: предмет Информатика
# Эксперт Гейтс Б.: предмет Информатика
# Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]
# Студент Гаврилов С.А.: оценки на лекциях: [2]; оценки за д/з: [3]