from typing import List, Tuple

class MaxPooling:
    Matrix = List[List[int]]
    def __init__(self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)) -> None:
        self.size = size
        self.step = step

    def __call__(self, matrix: Matrix) -> Matrix:
        if self.matrix_not_ok(matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")
        result = []
        rows, cols = len(matrix), len(matrix[0])
        for x in range(0, rows - self.size[0] + 1, self.step[0]):
            row = []
            for y in range(0, cols - self.size[1] + 1, self.step[1]):
                block = [matrix[i][j] for i in range(x, x + self.size[0]) for j in range(y, y + self.size[1])]
                row.append(max(block))
            result.append(row)
        return result

    @classmethod
    def matrix_not_ok(cls, matrix: Matrix) -> bool:
        if not matrix or len(set(len(row) for row in matrix)) != 1:
            return True
        if any(not (type(value) in (int, float)) for line in matrix for value in line):
            return True
        return False



########################################################################################################################

mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректно отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректно отработала проверка (или она отсутствует) на не числовые значения в матрице"

mp = MaxPooling(step=(1, 1), size=(5, 5))
res = mp([[5, 0, 88, 2, 7, 65],
          [1, 33, 7, 45, 0, 1],
          [54, 8, 2, 38, 22, 7],
          [73, 23, 6, 1, 15, 0],
          [4, 12, 9, 1, 76, 6],
          [0, 15, 10, 8, 11, 78]])  # [[88, 88], [76, 78]]

assert res == [[88, 88], [76, 78]], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"