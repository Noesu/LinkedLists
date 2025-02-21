from typing import Union


class Dimensions:
    Cm = Union[int, float]

    def __init__(self, a: Cm, b: Cm, c: Cm) -> None:
        if all(_ > 0 for _ in (a, b, c)):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    def __lt__(self, other):
        return hash(self) < hash(other)


s_inp = input()
lst_dims = sorted([Dimensions(*map(float, obj.split())) for obj in s_inp.split('; ')])