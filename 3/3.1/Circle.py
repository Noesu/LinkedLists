from typing import Union

class Circle:
    def __init__(self, x: Union[int, float], y: Union[int, float], radius: Union[int, float]) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def __setattr__(self, key: str, value: Union[int, float]) -> None:
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == "radius" and value < 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item: str) -> bool:
        return False

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, x: Union[int, float]) -> None:
        self.__x = x

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, y: Union[int, float]) -> None:
        self.__y = y

    @property
    def radius(self) -> Union[int, float]:
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[int, float]) -> None:
        self.__radius = radius

circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует