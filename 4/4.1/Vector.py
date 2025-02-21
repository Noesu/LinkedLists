from typing import Tuple, Union

class Vector:
    _allowed_types = (int, float)
    def __init__(self, *coords: Union[int, float]):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError('неверный тип координат')
        self._coords = coords

    def __len__(self) -> int:
        return len(self._coords)

    def __add__(self, other: Union["Vector", "VectorInt"]) -> Union["Vector", "VectorInt"]:
        self.__validate_vectors(other)
        if other._all_coords_are_int():
            return VectorInt(*(a + b for a, b in zip(self._coords, other._coords)))
        return Vector(*(a + b for a, b in zip(self._coords, other._coords)))

    def __sub__(self, other: Union["Vector", "VectorInt"]) -> Union["Vector", "VectorInt"]:
        self.__validate_vectors(other)
        if other._all_coords_are_int():
            return VectorInt(*(a - b for a, b in zip(self._coords, other._coords)))
        return Vector(*(a - b for a, b in zip(self._coords, other._coords)))

    def __validate_vectors(self, other: Union["Vector", "VectorInt"]) -> None:
        if not isinstance(other, Vector):
            raise TypeError("Операнд не является классом Vector")
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')

    def _all_coords_are_int(self) -> bool:
        return all(type(coord) == int for coord in self._coords)

    def get_coords(self) -> Tuple[Union[int, float], ...]:
        return tuple(self._coords)

class VectorInt(Vector):
    _allowed_types = (int, )

########################################################################################################################

v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (
4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(
    v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"