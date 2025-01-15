from typing import List, Union

class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key: str, value: Union[str, int]) -> None:
        if key == "title" and type(value) == str:
            object.__setattr__(self, key, value)
        elif key in {"practices", "duration"} and type(value) == int and 0 < value:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item: str) -> bool:
        return False

    def __delattr__(self, item: str) -> None:
        if item not in {"title", "practices", "duration"}:
            super().__delattr__(item)

class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons: List[LessonItem] = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules: List[Module] = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
