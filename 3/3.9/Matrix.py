from typing import List, Tuple, Union

class Matrix:
    Matrix2D = List[List[Union[int, float]]]
    Value = Union[int, float]
    Index = Tuple[int, int]

    def __init__(self, *args: Union[Matrix2D, Tuple[int, int, Value]]) -> None:
        # Валидация аргумента, если это готовая матрица
        if len(args) == 1 and isinstance(args[0], list):
            matrix = args[0]
            if not matrix:
                raise ValueError("Матрица не может быть пустой")
            if not all(type(row) is list for row in matrix):
                raise TypeError("Матрица должна быть списком списков")

            first_row_length = len(matrix[0])
            for row in matrix:
                if len(row) != first_row_length:
                    raise TypeError('список должен быть прямоугольным')
                for value in row:
                    self.__validate_value(value)
            self.list2D: Matrix.Matrix2D = matrix

        #Валидация аргумента, если это параметры матрицы
        elif len(args) == 3 and type(args[0]) is int and type(args[1]) is int and type(args[2]) in (int, float):
            rows, cols, fill_value = args
            self.list2D: Matrix.Matrix2D = [[fill_value for _ in range(cols)] for _ in range(rows)]
        else:
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    def __getitem__(self, item: Index) -> Value:
        row, col = self.__validate_index(item)
        return self.list2D[row][col]

    def __setitem__(self, key: Index, value: Value) -> None:
        row, col = self.__validate_index(key)
        self.__validate_value(value)
        self.list2D[row][col] = value

    def __add__(self, other: Union[int, "Matrix"]) -> "Matrix":
        if isinstance(other, Matrix):
            self.__validate_matrix_size(other)
            return Matrix([[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.list2D, other.list2D)])
        elif type(other) in (int, float):
            return Matrix([[a + other for a in row] for row in self.list2D])
        else:
            raise

    def __sub__(self, other: Union[int, "Matrix"]) -> "Matrix":
        if isinstance(other, Matrix):
            self.__validate_matrix_size(other)
            return Matrix([[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.list2D, other.list2D)])
        elif type(other) in (int, float):
            return Matrix([[a - other for a in row] for row in self.list2D])
        else:
            raise 

    def __validate_index(self, item: Index) -> Index:
        if len(item) != 2:
            raise TypeError(f'задан неверный индекс{item}')
        row, col = item
        if type(row) is not int or type(col) is not int:
            raise IndexError('значения матрицы должны быть числами')
        if not 0 <= row < len(self.list2D) or not 0 <= col < len(self.list2D[0]):
            raise IndexError('недопустимые значения индексов')
        return row, col

    def __validate_value(self, value: Value) -> None:
        if type(value) not in (int, float):
            raise TypeError('список должен быть состоящим из чисел')

    def __validate_matrix_size(self, other: "Matrix") -> None:
        if len(self.list2D) != len(other.list2D) or len(self.list2D[0]) != len(other.list2D[0]):
            raise ValueError('операции возможны только с матрицами равных размеров')




########################################################################################################################

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"