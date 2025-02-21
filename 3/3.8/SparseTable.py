from typing import Any, Callable, Dict, Tuple

Key = Tuple[int, int]

class Cell:
    def __init__(self, value: Any) -> None:
        self.value = value

def validate_index(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self, *args, **kwargs) -> Any:
        if isinstance(args[0], tuple):
            row, col = args[0][0], args[0][1]
        else:
            row, col = args[0], args[1]
        if any([type(row) != int, type(col) != int, row < 0, col < 0]):
            raise IndexError(f'Wrong cell address{row, col}')
        return func(self, *args)
    return wrapper


def check_cell_existence(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self, *args: Any) -> Any:
        if not tuple(args) in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        return func(self, *args)
    return wrapper

class SparseTable:
    def __init__(self) -> None:
        self.rows = 0
        self.cols = 0
        self.table: Dict[Key, Any] = dict()

    @property
    def rows(self):
        return max(key[0] for key in self.table) + 1

    @rows.setter
    def rows(self, value):
        self.__rows = value

    @property
    def cols(self):
        return max(key[1] for key in self.table) + 1

    @cols.setter
    def cols(self, value):
        self.__cols = value

    @validate_index
    def __getitem__(self, key: Key) -> Any:
        if key in self.table:
            return self.table[key]
        raise ValueError('данные по указанным индексам отсутствуют')

    @validate_index
    def __setitem__(self, key: Key, value: Any) -> None:
        self.table[key] = value

    @validate_index
    def add_data(self, row: int, col: int, data: Cell) -> None:
        self.table[(row, col)] = data

    @check_cell_existence
    @validate_index
    def remove_data(self, row: int, col: int) -> None:
        del self.table[(row, col)]

########################################################################################################################


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"



