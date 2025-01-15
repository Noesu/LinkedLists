from typing import Union

class Book:
    def __init__(self, title: str ='', author: str = '', pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key: str, value: Union[str, int]) -> None:
        if key in ("title", "author"):
            if type(value) == str:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in ("pages", "year"):
            if type(value) == int:
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")

book = Book("Python ООП", "Сергей Балакирев", 123, 2022)




