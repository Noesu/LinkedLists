from random import shuffle
from typing import Tuple


class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = True

    def __bool__(self):
        return not self.is_open

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int):
        if type(value) == int and 0 <= value <= 8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) == bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")


class GamePole:
    __field = None

    def __new__(cls, *args, **kwargs):
        if not cls.__field:
            cls.__field = super().__new__(cls)
        return cls.__field

    def __init__(self, n: int, m: int, total_mines: int) -> None:
        self.m = m
        self.n = n
        self.cells: int = n * m
        self.empty_cells: int = n * m - total_mines
        self.total_mines: int = total_mines
        self.pole: Tuple[Tuple[Cell, ...], ...] = tuple(tuple(Cell() for _ in range(m)) for _ in range(n))

    @property
    def pole(self) -> Tuple[Tuple[Cell, ...], ...]:
        return self.__pole_cells

    @pole.setter
    def pole(self, value: Tuple[Tuple[Cell, ...], ...]) -> None:
        self.__pole_cells = value

    def init_pole(self) -> None:
        # mines = sample([True, False], counts=[self.total_mines, self.empty_cells], k=self.cells)
        mines = [True] * self.total_mines + [False] * self.empty_cells
        shuffle(mines)

        mines_sequence = iter(mines)
        for line in self.pole:
            for cell in line:
                cell.is_mine = next(mines_sequence)
                cell.is_open = False

        for n in range(self.n):
            for m in range(self.m):
                self.pole[n][m].number = self.scan_mines(n, m)


    def scan_mines(self, n: int, m: int) -> int:
        sector = [(y, x)
                  for y in range(n - 1, n + 2)
                  for x in range(m - 1, m + 2)
                  if 0 <= y <= self.n - 1 and 0 <= x <= self.m - 1 and (x, y) != (m, n)
                  ]
        return sum(self.pole[cell[0]][cell[1]].is_mine for cell in sector)

    def open_cell(self, i: int, j: int):
        self.pole[i][j].is_open = True

    def show_pole(self) -> None:
        for line in self.pole:
            for cell in line:
                if cell.is_mine:
                    print('*', end='')
                elif cell.number:
                    print(cell.number, end='')
                else:
                    print('0', end='')
            print('')


########################################################################################################################

p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"