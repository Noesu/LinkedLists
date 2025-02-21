from typing import Any, Iterator, List

class TriangleListIterator:
    def __init__(self, lst: List[List[Any]]) -> None:
        self.lst = lst

    def __iter__(self) -> Iterator[Any]:
        self.line = 0
        self.item = 0
        return self

    def __next__(self) -> Any:
        if self.line >= len(self.lst):
            raise StopIteration
        value = self.lst[self.line][self.item]
        self.item += 1
        if self.item >= len(self.lst[self.line]):
            self.line += 1
            self.item = 0
        return value


########################################################################################################################

lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]
it = TriangleListIterator(lst)

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)