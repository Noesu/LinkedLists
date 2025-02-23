from collections import deque
from typing import Tuple, Union

Coord = Union[int, float]

class PointTrack:
    def __init__(self, x: Coord, y: Coord) -> None:
        if not all(type(coord) in (int, float) for coord in (x, y)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.x}, {self.y}'


class Track:
    def __init__(self, *args: Union[Tuple[Coord, Coord], Tuple[PointTrack, ...]]) -> None:
        self.__points: deque = deque()
        if isinstance(args[0], tuple) and len(args) == 2:
            self.__points.append(PointTrack(*args[0]))
        else:
            for arg in args:
                self.__points.append(arg)

    @property
    def points(self) -> Tuple[PointTrack, ...]:
        return tuple(self.__points)

    def add_back(self, point: PointTrack) -> None:
        if isinstance(point, PointTrack):
            self.__points.append(point)

    def add_front(self, point: PointTrack) -> None:
        if isinstance(point, PointTrack):
            self.__points.appendleft(point)

    def pop_back(self) -> None:
        if self.__points:
            self.__points.pop()

    def pop_front(self) -> None:
        if self.__points:
            self.__points.popleft()

########################################################################################################################

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)