from typing import Any, List

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self) -> "StackObj":
        return self.__next

    @next.setter
    def next(self, value: "StackObj") -> None:
        self.__next = value

class Stack:
    def __init__(self):
        self.top = None

    def __add__(self, other: StackObj) -> "Stack":
        self.push_back(other)
        return self

    def __mul__(self, dataset: List[Any]):
        for data in dataset:
            self.push_back(StackObj(data))
        return self

    def push_back(self, obj: StackObj) -> None:
        if not self.top:
            self.top = obj
        else:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj

    def pop_back(self) -> None:
        if self.top:
            node = prev_node = self.top
            while node.next:
                prev_node = node
                node = node.next
            if node == prev_node:
                self.top = None
            prev_node.next = None



########################################################################################################################

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']
st += StackObj("225")
st.pop_back()

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"