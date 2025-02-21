from math import sqrt
from typing import Any, Optional, Type, Union

Cm = Union[int, float]

class Descriptor:
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self.name = name

    def __get__(self, instance: Any, owner: Type[Any]) -> Cm:
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: Cm) -> None:
        if value <= 0:
            raise ValueError("Длины сторон треугольника должны быть положительными числами")

        sides: dict[str, Optional[Cm]] = {side: instance.__dict__.get(side) for side in ("a", "b", "c")}
        sides[self.name] = value  # Подставляем новое значение

        if all(sides.values()):
            a, b, c = sides["a"], sides["b"], sides["c"]
            if not (a < b + c and b < a + c and c < a + b):
                raise ValueError("С указанными длинами нельзя образовать треугольник")

        instance.__dict__[self.name] = value


class Triangle:
    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a: Cm, b: Cm, c: Cm) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __len__(self) -> int:
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs) -> float:
        return self.tr()

    def tr(self) -> float:
        p: float = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

########################################################################################################################

tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули не верные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула не верное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул не верное значение"

tr = Triangle(3.4, 4, 5)
assert len(tr) == 12, "функция len вернула не верное значение для треугольника со сторонами (3.4, 4, 5)"
assert 6.7 < tr() < 6.8, "метод __call__ вернул не верное значение для треугольника со сторонами (3.4, 4, 5)"

try:
    tr.a = 1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'a'"

try:
    tr.b = 1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'b'"

try:
    tr.c = 0.1
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'c'"

try:
    tr.b = -4
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при изменении атрибута 'b'"