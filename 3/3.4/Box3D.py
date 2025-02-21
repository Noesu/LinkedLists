from typing import Union


class Box3D:
    Size = Union[int, float]

    def __init__(self, w: Size, h: Size, d: Size) -> None:
        self.depth = d
        self.height = h
        self.width = w

    def __add__(self, other: "Box3D") -> "Box3D":
        return Box3D(*(s1 + s2 for s1, s2 in
                       zip([self.width, self.height, self.depth], [other.width, other.height, other.depth])))

    def __mul__(self, other: Size) -> "Box3D":
        return Box3D(*(s1 * other for s1 in [self.width, self.height, self.depth]))

    def __rmul__(self, other: Size) -> "Box3D":
        return Box3D(*(s1 * other for s1 in [self.width, self.height, self.depth]))

    def __sub__(self, other: "Box3D") -> "Box3D":
        return Box3D(*(s1 - s2 for s1, s2 in
                       zip([self.width, self.height, self.depth], [other.width, other.height, other.depth])))

    def __floordiv__(self, other: Size) -> "Box3D":
        return Box3D(*(s1 // other for s1 in [self.width, self.height, self.depth]))

    def __mod__(self, other: Size) -> "Box3D":
        return Box3D(*(s1 % other for s1 in [self.width, self.height, self.depth]))


########################################################################################################################

box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3  # Box3D: width=2, height=1, depth=0

if __name__ == "__main__":
    box1 = Box3D(1, 2, 3)
    box2 = Box3D(2, 4, 6)

    box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
    assert box.width == 3, "неверное значение атрибута width"
    assert box.height == 6, "неверное значение атрибута height"
    assert box.depth == 9, "неверное значение атрибута depth"

    box = box1 * 2  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
    assert box.width == 2, "неверное значение атрибута width"
    assert box.height == 4, "неверное значение атрибута height"
    assert box.depth == 6, "неверное значение атрибута depth"

    box = 3 * box2  # Box3D: width=6, height=12, depth=18
    assert box.width == 6, "неверное значение атрибута width"
    assert box.height == 12, "неверное значение атрибута height"
    assert box.depth == 18, "неверное значение атрибута depth"

    box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
    assert box.width == 1, "неверное значение атрибута width"
    assert box.height == 2, "неверное значение атрибута height"
    assert box.depth == 3, "неверное значение атрибута depth"

    box = box1 // 2  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
    assert box.width == 0, "неверное значение атрибута width"
    assert box.height == 1, "неверное значение атрибута height"
    assert box.depth == 1, "неверное значение атрибута depth"

    box = box2 % 3  # Box3D: width=2, height=1, depth=0
    assert box.width == 2, "неверное значение атрибута width"
    assert box.height == 1, "неверное значение атрибута height"
    assert box.depth == 0, "неверное значение атрибута depth"
