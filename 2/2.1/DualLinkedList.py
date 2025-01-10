from datetime import datetime
import random
from string import ascii_letters, digits


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
        else:
            self.head = obj
        self.tail = obj
        self.size += 1

    def remove_obj(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            prev = self.tail.get_prev()
            prev.set_next(None)
            self.tail = prev
        self.size -= 1

    def insert_obj(self, obj, position: int):
        """Вставляет данные перед элементом position"""

        # Обработка исключения выхода индекса за пределы списка
        if position < 0 or position > self.size:
            raise IndexError(f"Индекс ({position}) выходит за пределы списка ({self.size}).")

        # Поиск позиции с головы
        if position <= self.size // 2:
            node = self.head
            for _ in range(position):
                node = node.get_next()
        # Поиск позиции с хвоста
        else:
            node = self.tail
            for _ in range(self.size - position):
                node = node.get_prev()

        # Вставка объекта по индексу
        prev_node = node.get_prev()
        if prev_node:
            prev_node.set_next(obj)
            obj.set_prev(prev_node)
        else:
            self.head = obj

        obj.set_next(node)
        node.set_prev(obj)

        self.size += 1

    def get_data(self):
        data = []
        node = self.head
        while node:
            data.append(node.get_data())
            node = node.get_next()
        return data


########################################################################################################################

K_VALUE = 1000
L_VALUE = 10000
symbols = ascii_letters + digits




print(f"\n1. Создание списка из {L_VALUE} элементов, по {K_VALUE} случайных символов в каждом:")
DATA = [''.join(random.choices(symbols, k=K_VALUE)) for _ in range(L_VALUE)]

start = datetime.now()
lst1 = LinkedList()
for data in DATA:
    lst1.add_obj(ObjList(data))
finish = datetime.now()
print(f"    - с двусвязным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")

start = datetime.now()
lst2 = []
for data in DATA:
    lst2.append(data)
finish = datetime.now()
print(f"    - со стандартным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")




print(f"\n2. Удаление {L_VALUE // 2} последних элементов из списка:")

start = datetime.now()
for _ in range(L_VALUE // 2):
    lst1.remove_obj()
finish = datetime.now()
print(f"    - с двусвязным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")

start = datetime.now()
for _ in range(L_VALUE // 2):
    lst2.pop()
finish = datetime.now()
print(f"    - со стандартным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")




print(f"\n3. Вставка {L_VALUE // 2} элементов на случайные позиции")

start = datetime.now()
for data in DATA[:L_VALUE // 2]:
    lst1.insert_obj(ObjList(data), random.randint(0, lst1.size))
finish = datetime.now()
print(f"    - с двусвязным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")

start = datetime.now()
for data in DATA[:L_VALUE // 2]:
    lst2.insert(random.randint(0, len(lst2)), ObjList(data))
finish = datetime.now()
print(f"    - со стандартным списком: {(finish - start).total_seconds() * 1000:.2f} мс.")
