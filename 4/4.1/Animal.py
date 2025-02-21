from typing import Tuple

class Animal:
    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old

    def get_info(self) -> str:
        return repr(self)

class Cat(Animal):
    def __init__(self, name: str, old: int, color: str, weight: int) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'

class Dog(Animal):
    def __init__(self, name: str, old: int, breed: str, size: Tuple[int, int]) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def __repr__(self) -> str:
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'

########################################################################################################################

cat = Cat("cat", 5, "green", 2)
print(cat.get_info())
assert cat.get_info() == 'cat: 5, green, 2', "метод get_info вернул неверные данные"
