from math import sqrt
from time import monotonic
from typing import List, Union

class LineTo:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y

class PathLines:
    def __init__(self, *lines: LineTo) -> None:
        self.lines: List[LineTo] = list(lines)

    def get_path(self) -> List[LineTo]:
        return self.lines

    def get_length(self) -> float:
        length = prev_x = prev_y = 0.0

        for line in self.lines:
            length += sqrt(pow((line.x - prev_x), 2) + pow((line.y - prev_y), 2))
            prev_x, prev_y = line.x, line.y
        return length

    def add_line(self, line: LineTo) -> None:
        self.lines.append(line)

########################################################################################################################
#
# start = monotonic()
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print((monotonic() - start) * 1000)