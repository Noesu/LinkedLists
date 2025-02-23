from abc import ABC, abstractmethod
from typing import Optional, Tuple

class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj: "StackObj") -> None: pass

    @abstractmethod
    def pop_back(self) -> Optional["StackObj"]: pass

class StackObj:
    def __init__(self, data: str) -> None:
        self._data = data
        self._next: Optional[StackObj] = None

    @property
    def next(self) -> Optional["StackObj"]:
        return self._next

    @next.setter
    def next(self, value: Optional["StackObj"]):
        self._next = value

class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def _get_last_nodes(self) -> Tuple[Optional[StackObj], Optional[StackObj]]:
        """Метод поиска конца списка. Возвращает:
        None, node - если в списке один элемент
        node, node - если в списке два и более элемента
        """
        prev_node = None
        node = self._top
        while node and node.next:
            prev_node = node
            node = node.next
        return prev_node, node

    def push_back(self, obj: StackObj) -> None:
        _, last_node = self._get_last_nodes()
        if last_node:
            last_node.next = obj
        else:
            self._top = obj

    def pop_back(self) -> Optional[StackObj]:
        if not self._top:       # Если список пустой
            return None
        node, last_node = self._get_last_nodes()
        if not node:            # Если в списке один элемент
            self._top = None
        else:                   # Если в списке два и более элемента
            node.next = None
        return last_node


########################################################################################################################

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"