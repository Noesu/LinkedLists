from typing import Any, Iterable
from typing_extensions import Self

class Tuple(tuple):
    def __new__(cls, values: Iterable[Any]) -> Self:
        return super().__new__(cls, tuple(values))

    def __add__(self, other: Iterable[Any])-> "Tuple":
        return Tuple(super().__add__(tuple(other)))


########################################################################################################################

t = Tuple([1, 2, 3])
print(type(t))
t = t + "Python"
print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
print(type(t))
print(t)