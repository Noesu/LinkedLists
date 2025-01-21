from typing import Dict, Optional, Union

class ObjList:
    def __init__(self, data: str) -> None:
        self.data: str = data
        self.prev: Optional[ObjList] = None
        self.next: Optional[ObjList] = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, value: str):
        self.__data = value

    @property
    def prev(self) -> "ObjList":
        return self.__prev

    @prev.setter
    def prev(self, value: "ObjList"):
        self.__prev = value

    @property
    def next(self) -> "ObjList":
        return self.__next

    @next.setter
    def next(self, value: "ObjList"):
        self.__next = value

class LinkedList:
    def __init__(self, head: Optional[ObjList]=None, tail: Optional[ObjList]=None) -> None:
        self.head = head
        self.tail = tail

    def __len__(self) -> int:
        return self.count_nodes().get("count") + 1

    def __call__(self, indx: int) -> str:
        if 0 < indx < len(self):
            return self.count_nodes(indx).get("node").data
        else:
            raise ValueError(f'Запрошенный индекс ({indx}) вне диапазона.')

    def count_nodes(self, indx: Optional[int]=None) -> Dict[str, Union[int, Optional[ObjList]]]:
        count = 0
        node = None
        if self.head:
            node = self.head
            while node.next:
                node = node.next
                count += 1
                if count == indx:
                    break
        return {"count": count, "node": node}

    def add_obj(self, obj: ObjList) -> None:
        if not self.head:
            self.head = obj
        else:
            node = self.tail
            node.next = obj
            obj.prev = self.tail
        self.tail = obj

    def remove_obj(self, indx: int):
        list_len = len(self)
        if not 0 <= indx < list_len:
            raise ValueError(f'Запрошенный индекс ({indx}) вне диапазона. Актуальная длина списка: {list_len}')

        node = self.count_nodes(indx=indx).get('node')
        if node.prev is None:
            if node.next is None:
                self.head = self.tail = None
            else:
                self.head = node.next
        else:
            if node.next is None:
                self.tail = node.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev


########################################################################################################################

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
print(len(ln))
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"


h = LinkedList()
h.add_obj(ObjList('Hello'))
h.remove_obj(0)
print(h.__dict__)  # {'_LinkedList__head': None, '_LinkedList__tail': None}