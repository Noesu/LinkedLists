from typing import Tuple, Union

class Track:
    Coord = Union[int, float]
    Kmh = Union[int, float]
    def __init__(self, start_x: Coord, start_y: Coord) -> None:
        self.__tracklist = []

    def __getitem__(self, indx: int) -> Tuple[Tuple[Coord, Coord], Kmh]:
        self.__validate_index(indx)
        return self.__tracklist[indx]

    def __setitem__(self, indx: int, value: Kmh):
        self.__validate_index(indx)
        self.__tracklist[indx][1] = value

    def __len__(self) -> int:
        return len(self.__tracklist)

    def add_point(self, x: Coord, y: Coord, speed: Kmh) -> None:
        self.__tracklist.append([(x, y), speed])

    def __validate_index(self, indx: int):
        if type(indx) != int or not (-len(self) <= indx < len(self)):
            raise IndexError('некорректный индекс')

########################################################################################################################

# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
#
# tr[2] = 60
# c, s = tr[2]
# print(c, s)
#
# res = tr[3] # IndexError

########################################################################################################################

tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
c, s = tr[0]
assert c == (20, 0) and s == 100, "Неверно работает add_point"
tr[0] = 120
c, s = tr[0]
assert c == (20, 0) and s == 120, "Неверно работает __getitem__/__setitem__"

tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

try:
    res = tr[3]  # IndexError
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

print('Ok')
