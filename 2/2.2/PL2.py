from math import sqrt
from time import monotonic
from typing import List, Union, Optional

class LineTo:
    def __init__(self, x: Union[int, float], y: Union[int, float], node: Optional["LineTo"] = None) -> None:
        self.x = x
        self.y = y
        self.next = node

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: Union[int, float]):
        self.__x = float(x)

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: Union[int, float]):
        self.__y = float(y)

    @property
    def next(self) -> Optional["LineTo"]:
        return self.__next

    @next.setter
    def next(self, next_line: Optional["LineTo"]):
        self.__next = next_line


class PathLines:
    def __init__(self, *lines: LineTo) -> None:
        prev = self.head = LineTo(0, 0)
        self.tail = None
        for node in lines:
            prev.next = node
            prev = node
            self.tail = node

    def get_path(self) -> List[LineTo]:
        lines = []
        node = self.head
        while node:
            lines.append(node)
            node = node.next
        return lines

    def get_length(self) -> float:
        length = prev_x = prev_y = 0.0
        node = self.head
        while node:
            length += sqrt(pow((node.x - prev_x), 2) + pow((node.y - prev_y), 2))
            prev_x, prev_y = node.x, node.y
            node = node.next
        return length

    def add_line(self, line: LineTo) -> None:
        if self.tail:
            self.tail.next = line
        else:
            self.tail = line


########################################################################################################################

start = monotonic()
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print((monotonic() - start) * 1000)