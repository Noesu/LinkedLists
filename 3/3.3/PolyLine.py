from typing import List, Tuple

class PolyLine:
    def __init__(self, *coords: Tuple[int, int]) -> None:
        self.coords: List[Tuple[int, int]] = list(coords)

    def add_coord(self, x: int, y: int) -> None:
        self.coords.append((x, y))

    def remove_coord(self, indx: int) -> None:
        self.coords.pop(indx)

    def get_coords(self) -> List[Tuple[int, int]]:
        return self.coords

########################################################################################################################

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
assert hasattr(poly, 'add_coord') and hasattr(poly, 'remove_coord') and hasattr(poly, 'get_coords') and \
       callable(poly.add_coord) and callable(poly.remove_coord) and callable(poly.get_coords), \
    "ошибка, не все методы есть в экземпляре класса"

poly.get_coords()
assert poly.get_coords() == [(1, 2), (3, 5), (0, 10), (-1, 8)], \
    "метод get_coords() вернул неправильный формат данных"

poly.add_coord(10, 20)
assert poly.get_coords()[-1] == (10, 20), "метод add_coord() работает некорректно"

poly.remove_coord(0)
poly.remove_coord(-1)
assert poly.get_coords() == [(3, 5), (0, 10), (-1, 8)], "метод remove_coord() работает некорректно"
print("Правильный ответ !!")