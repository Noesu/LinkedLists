from typing import Tuple

class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

class StringValue:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != str:
            raise ValueError('возможны только строковые значения')
        setattr(instance, self.name, value)

class CellInteger:
    value = IntegerValue()
    def __init__(self, start_value = 0):
        self.value = start_value

class CellString:
    value = StringValue()
    def __init__(self, start_value = ''):
        self.value = start_value

class TableValues:
    def __init__(self, r: int, c: int, cell: type = None) -> None:
        if not cell:
            raise ValueError('параметр cell не указан')
        self.__rows = r
        self.__cols = c
        self.cells = tuple(tuple(cell() for _ in range(c)) for _ in range(r))

    def __setitem__(self, key: Tuple, value):
        self.cells[key[0]][key[1]].value = value

    def __getitem__(self, key: Tuple):
        return self.cells[key[0]][key[1]].value


########################################################################################################################

# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
# table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError
#
# # вывод таблицы в консоль
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()

########################################################################################################################

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

try:
    tb[2, 1] = 1.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

for row in tb.cells:
    for x in row:
        assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

cell = CellInteger(10)
assert cell.value == 10, "дескриптор value вернул неверное значение"