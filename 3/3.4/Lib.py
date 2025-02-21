from typing import Union

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.year = year
        self.author = author
        self.title = title


class Lib:
    def __init__(self) -> None:
        self.book_list = []

    def __add__(self, other: Book):
        self.book_list.append(other)
        return self

    def __sub__(self, other: Union[Book, int]):
        if type(other) == int:
            self.book_list.pop(other)
            return self
        elif type(other) == Book:
            self.book_list.remove(other)
            return self
        else:
            raise ValueError(f"Wrong argument type: {type(other)}")

    def __len__(self) -> int:
        return len(self.book_list)



########################################################################################################################

lib = Lib()
b1 = Book('Бойцовский клуб', 'Чак Паланик', 1996)
b2 = Book('Виктор Пелевин', 'Generation "П"', 1999)
lib_id = id(lib)
# TEST-TASK-ADD___________________________________
lib += b1
lib += b2
assert (len(lib.__dict__['book_list'])) == 2 and [isinstance(l, Book) for l in lib.__dict__], "ошибка в add"
assert (lib_id == id(lib)), "ошибка в id add"
# TEST-TASK-SUB-BOOK___________________________________
lib -= b1
assert b2 not in lib.__dict__, "ошибка в sub-book"
assert (lib_id == id(lib)), "ошибка в id sub-book"
# TEST-TASK-SUB-INDEX___________________________________
lib -= 0
assert lib.book_list == [], "ошибка в sub-index"
assert (lib_id == id(lib)), "ошибка в id sub-index"
# TEST-TASK-LEN___________________________________
assert len(lib) == 0, "ошибка в len"
# ___________________________________
print("Молодец! Решение правильное!")