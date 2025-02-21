from typing import Any, Union

F_unit = Union[int, float]

class Furniture:
    def __init__(self, name: str, weight: F_unit) -> None:
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    def __setattr__(self, key: str, value: Any):
        if key == "_Furniture__name":
            self.__verify_name(value)
        if key == "_Furniture__weight":
            self.__verify_weight(value)
        super().__setattr__(key, value)

    @staticmethod
    def __verify_name(name: str) -> None:
        if type(name) is not str:
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight: F_unit) -> None:
        if type(weight) not in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self) -> tuple:
        return tuple(self.__dict__.values())

class Closet(Furniture):
    def __init__(self, name: str, weight: F_unit, tp: bool, doors: int) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture):
    def __init__(self, name: str, weight: F_unit, height: F_unit) -> None:
        super().__init__(name, weight)
        self._height = height

class Table(Furniture):
    def __init__(self, name: str, weight: F_unit, height: F_unit, square: F_unit) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square


########################################################################################################################

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())