from typing import List, Type, Union

class Integer:
    def __init__(self, start_value: int = 0) -> None:
        self.value = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value

    def __repr__(self) -> str:
        return str(self.__value)

class Float:
    def __init__(self, start_value: float = 0.0) -> None:
        self.value = start_value

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        if type(value) != float:
            raise ValueError('должно быть число с плавающей точкой')
        self.__value = value

    def __repr__(self) -> str:
        return str(self.__value)

class Array:
    def __init__(self, max_length: int, cell: Type[Union[Integer, Float]]) -> None:
        self.__max_length = max_length
        self.__cell = cell
        if cell in (Integer, Float):
            self.__values: List[Union[Integer, Float]] = [self.__cell() for _ in range(max_length)]
        else:
            raise ValueError(f'Wrong cell type: {cell}')

    def __setitem__(self, key: int, value: Union[int, float]) -> None:
        self.__validate(key)
        self.__values[key].value = value

    def __getitem__(self, key: int) -> Union[int, float]:
        self.__validate(key)
        return self.__values[key].value

    def __repr__(self) -> str:
        return " ".join(map(str, self.__values))

    def __validate(self, item) -> None:
        if type(item) != int or not (-self.__max_length <= item < self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

########################################################################################################################

# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError

########################################################################################################################

print("Проверка целых чисел...")

a = Array(20, cell=Integer)

assert a[18] == 0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

a[0] = 1
a[1] = 2
assert str(a) == "1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1 and a[1] == 2, "некорректно работает запись и/или считывание значений из массива по индексу"


try:
    a[1] = 2.5
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a[100] = 25
except IndexError as err:
    assert str(err) == 'неверный индекс для доступа к элементам массива', "не сгенерировалось исключение IndexError при записи"


try:
    print(a[100])
except IndexError as err:
    assert str(err) == 'неверный индекс для доступа к элементам массива', "не сгенерировалось исключение IndexError при чтении"

print("Проверка пройдена.")
print()

#-----------------------------
try:
    x = Float()
except:
    print("class Float не определён")
    raise SystemExit(0)
#-----------------------------

print("Проверка вещественных чисел...")

a = Array(20, cell=Float)
assert a[18] == 0.0, "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.0"

a = Array(2, cell=Float)
a[0] = 1.0
a[1] = 2.0
print(str(a))
assert str(a) == "1.0 2.0", "функция str(a) для объекта класса Array вернула неверное значение"
assert a[0] == 1.0 and a[1] == 2.0, "некорректно работает запись и/или считывание значений из массива по индексу"

try:
    a[1] = 2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    a[100] = 25.5
except IndexError as err:
    assert str(err) == 'неверный индекс для доступа к элементам массива', "не сгенерировалось исключение IndexError при записи"

try:
    print(a[100])
except IndexError as err:
    assert str(err) == 'неверный индекс для доступа к элементам массива', "не сгенерировалось исключение IndexError при чтении"

print("Проверка пройдена.")
