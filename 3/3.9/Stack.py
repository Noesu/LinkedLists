from typing import Optional

class StackObj:
    def __init__(self, data: str):
        self.data: str = data
        self.next: Node = None
        self.prev: Node = None

Node = Optional[StackObj]

class Stack:
    def __init__(self) -> None:
        self.top: Optional[StackObj] = None
        self.tail: Optional[StackObj] = None
        self.length: int = 0

    def __getitem__(self, indx: int) -> str:
        return self.__get_node(indx).data

    def __setitem__(self, indx: int, value: str):
        self.__get_node(indx).data = value

    def __iter__(self) -> StackObj:
        for i in range(self.length):
            yield self.__get_node(i)

    def __get_node(self, indx: int) -> StackObj:
        if not type(indx) == int or not(0 <= indx < self.length):
            raise IndexError('неверный индекс')
        if indx <= self.length // 2:
            count = 0
            node = self.top
            while count != indx:
                node = node.next
                count += 1
        else:
            node = self.tail
            count = self.length - 1
            while count != indx:
                node = node.prev
                count -= 1
        return node

    def __open_stack(self, node: StackObj) -> None:
        self.top = node
        self.tail = node
        self.length += 1

    def push_back(self, node: StackObj) -> None:
        if not self.top and not self.tail:
            self.__open_stack(node)
            return
        prev_node = self.tail
        self.tail = node
        self.tail.prev = prev_node
        prev_node.next = self.tail
        self.length += 1

    def push_front(self, node: StackObj) -> None:
        if not self.top and not self.tail:
            self.__open_stack(node)
            return
        next_node = self.top
        self.top = node
        self.top.next = next_node
        next_node.prev = self.top
        self.length += 1

########################################################################################################################

st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"