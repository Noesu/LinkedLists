from typing import Any, Callable, Tuple

class Cell:
    def __init__(self, data: Any=0) -> None:
        self.data = data

    @property
    def data(self) -> Any:
        return self.__data

    @data.setter
    def data(self, value: Any) -> None:
        self.__data = value

def validate_index(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self, *args, **kwargs):
        row, col = args[0]
        if type(row) == int and type(col) == int and 0 <= row <= len(self.scheme) and 0 <= col < len(self.scheme[0]):
            return func(self, *args, **kwargs)
        raise IndexError('неверный индекс')
    return wrapper


class TableValues:

    Indx = Tuple[int, int]

    def __init__(self, rows: int, cols: int, type_data=int) -> None:
        self.scheme: Tuple[Tuple[Cell, ...], ...] = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))
        self.type_data = type_data
        self.rows = rows
        self.cols = cols

    @validate_index
    def __setitem__(self, indx: Indx, value: Any) -> None:
        if type(value) is not self.type_data:
            raise TypeError('неверный тип присваиваемых данных')
        row, col = indx
        self.scheme[row][col].data = value

    @validate_index
    def __getitem__(self, indx: Indx) -> Any:
        row, col = indx
        return self.scheme[row][col].data

    def __iter__(self) -> "TableValues":
        self.row = -1
        return self

    def __next__(self) -> Tuple[Any, ...]:
        self.row += 1
        if self.row >= self.rows:
            raise StopIteration
        return tuple(cell.data for cell in self.scheme[self.row])

########################################################################################################################

tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

