class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def next(self) -> "StackObj":
        return self.__next

    @next.setter
    def next(self, value: "StackObj") -> None:
        self.__next = value

    @property
    def data(self) -> "StackObj":
        return self.__data

    @data.setter
    def data(self, value: "StackObj") -> None:
        self.__data = value

class Stack:
    def __init__(self):
        self.top = None

    def __setitem__(self, key: int, value: StackObj) -> None:
        self.locate(key).data = value.data

    def __getitem__(self, key: int) -> StackObj:
        return self.locate(key)

    def locate(self, indx: int) -> StackObj:
        if indx < 0:
            raise IndexError("Некорректный индекс")
        node = self.top
        while node:
            if not indx:
                return node
            indx -= 1
            node = node.next
        raise IndexError("Элемент отсутствует в списке")

    def push(self, obj: StackObj) -> None:
        if not self.top:
            self.top = obj
        else:
            node = self.top
            while node.next:
                node = node.next
            node.next = obj

    def pop(self) -> None:
        if self.top:
            node = prev_node = self.top
            while node.next:
                prev_node = node
                node = node.next
            if node == prev_node:
                self.top = None
            output = prev_node.next
            prev_node.next = None
            return output


########################################################################################################################


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
print(st[0].data)
print(st[1].data)
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
