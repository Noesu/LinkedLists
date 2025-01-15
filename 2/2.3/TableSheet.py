from typing import Any, List

class FloatValue:
    @classmethod
    def check_data_type(cls, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner: Any, name: str) -> None:
        self.name = "_" + name

    def __get__(self, instance: Any, owner: Any) -> float:
        return getattr(instance, self.name)

    def __set__(self, instance: Any, value: float) -> None:
        self.check_data_type(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value: float = 0.0) -> None:
        self.value = value

class TableSheet:
    def __init__(self, n: int, m: int) -> None:
        self.cells: List[List[Cell]] = [[Cell(float()) for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)
values = iter(range(1, 16))

for line in table.cells:
    for cell in line:
        cell.value = float(next(values))

########################################################################################################################

assert isinstance(table, TableSheet)

assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
