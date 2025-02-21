from typing import Union

def validate(func):
    def wrapper(self, other):
        if isinstance(other, Vector):
            if len(self.coords) != len(other.coords):
                raise ArithmeticError('размерности векторов не совпадают')
        return func(self, other)
    return wrapper

class Vector:
    def __init__(self, *args):
        self.coords = tuple(args)

    @validate
    def __add__(self, other: "Vector"):
        return type(self)(*(x + y for x, y in zip(self.coords, other.coords)))

    @validate
    def __iadd__(self, other: Union[int, "Vector"]) -> "Vector":
        if isinstance(other, int):
            self.coords = tuple(x + other for x in self.coords)
        else:
            self.coords = tuple([x + y for x, y in zip(self.coords, other.coords)])
        return self

    @validate
    def __sub__(self, other: "Vector"):
        return type(self)(*(x - y for x, y in zip(self.coords, other.coords)))

    @validate
    def __isub__(self, other: Union[int, "Vector"]) -> "Vector":
        if isinstance(other, int):
            self.coords = tuple(x - other for x in self.coords)
        else:
            self.coords = tuple([x - y for x, y in zip(self.coords, other.coords)])
        return self

    @validate
    def __mul__(self, other: "Vector"):
        return type(self)(*(x * y for x, y in zip(self.coords, other.coords)))

    def __eq__(self, other: "Vector") -> bool:
        return self.coords == other.coords




########################################################################################################################

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True