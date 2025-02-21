from typing import Union

class Dimensions:
    Cm = Union[int, float]
    MIN_DIMENSION: Cm = 10
    MAX_DIMENSION: Cm = 10000

    def __init__(self, a: Cm, b: Cm, c: Cm) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def fit_dimensions(cls, value: Cm) -> bool:
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    def volume(self) -> Cm:
        return self.a * self.c * self.c

    @property
    def a(self) -> Cm:
        return self.__a

    @a.setter
    def a(self, value: Cm) -> None:
        if self.fit_dimensions(value):
            self.__a = value

    @property
    def b(self) -> Cm:
        return self.__b

    @b.setter
    def b(self, value: Cm) -> None:
        if self.fit_dimensions(value):
            self.__b = value

    @property
    def c(self) -> Cm:
        return self.__c

    @c.setter
    def c(self, value: Cm) -> None:
        if self.fit_dimensions(value):
            self.__c = value

    def __ge__(self, other: "Dimensions") -> bool:
        return self.volume() >= other.volume()

    def __gt__(self, other: "Dimensions") -> bool:
        return self.volume() > other.volume()


class ShopItem:
    def __init__(self, name: str, price: Union[int, float], dim: Dimensions) -> None:
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda item: item.dim)
print(lst_shop_sorted)
