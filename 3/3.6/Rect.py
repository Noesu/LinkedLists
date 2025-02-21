from typing import Union


class Rect:
    C = Union[int, float]

    def __init__(self, x: C, y: C, w: C, h: C) -> None:
        self.height = h
        self.width = w
        self.y = y
        self.x = x

    def __hash__(self):
        return hash((self.width, self.height))

########################################################################################################################

r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2