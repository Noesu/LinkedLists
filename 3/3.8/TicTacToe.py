class Cell:
    def __init__(self):
        self.reset()

    def __bool__(self):
        return self.is_free

    def reset(self):
        self.is_free = True
        self.value = 0


class TicTacToe:
    @staticmethod
    def validate_cell_exists(func):
        def wrapper(self, coords, *args, **kwargs):
            r, c = coords
            if isinstance(r, slice) or isinstance(c, slice):
                return func(self, coords, *args, **kwargs)
            if len(coords) != 2 or not (0 <= r < 3 and 0 <= c < 3):
                raise IndexError("неверный индекс клетки")
            return func(self, coords, *args, **kwargs)
        return wrapper


    @staticmethod
    def validate_cell_is_free(func):
        def wrapper(self, coords, *args, **kwargs):
            r, c = coords
            if not self.pole[r][c].is_free:
                raise ValueError('клетка уже занята')
            return func(self, coords, *args, **kwargs)
        return wrapper


    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    @validate_cell_exists
    def __getitem__(self, coords):
        r, c = coords
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))
        return self.pole[r][c].value

    @validate_cell_is_free
    @validate_cell_exists
    def __setitem__(self, coords, value):
        r, c = coords
        self.pole[r][c].value = value
        self.pole[r][c].is_free = False

    def clear(self):
        for r in self.pole:
            for c in r:
                c.reset()

########################################################################################################################

g = TicTacToe()
g.clear()
print(g[0, 0])
print(g[2, 2])

assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

print(g[0, :])
assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"