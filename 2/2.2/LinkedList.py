class StackObj:
    def __init__(self, data):
        self.__next = None
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, (StackObj, type(None))):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj: StackObj) -> None:
        if not self.top:                # Если список пустой
            self.top = obj                  # Объект становится первым
        else:                           # Если список не пустой
            node = self.top                 # Курсор текущего элемента устанавливаются на первый элемент списка
            while node.next:                # Пока текущий элемент имеет указатель на следующий элемент
                node = node.next                # Курсор текущего элемента устанавливается на следующий элемент
            node.next = obj                 # Текущему элементу присваивается ссылка на объект


    def pop(self) -> StackObj:
        if self.top:                    # Если список не пустой
            node = prev = self.top          # Курсоры текущего и предыдущего элемента устанавливаются на первый элемент списка
            while node.next:                # Пока текущий элемент имеет указатель на следующий элемент
                prev = node                     # Курсор предыдущего элемента устанавливается на текущий элемент
                node = node.next                # Курсор текущего элемента устанавливается на следующий элемент
            prev.next = None                # У предыдущего элемента удаляется ссылка на следующий элемент
            if prev == node:                # Если оба курсора указывают на один объект
                self.top = None                 # Удаляется указатель первого объекта
            return node                     # Возвращается удалённый элемент списка

    def get_data(self):
        data = []                           # Создается пустой список вывода
        if self.top:                        # Если список не пустой
            node = self.top                     # Курсор текущего элемента устанавливаются на первый элемент списка
            while node.next:                    # Пока текущий элемент имеет указатель на следующий элемент
                data.append(node.data)              # В список вывода добавляются данные на которые указывает курсор
                node = node.next                    # Курсор текущего элемента устанавливается на следующий элемент
            data.append(node.data)              # К списку вывода добавляются данные последнего элемента
        return data


########################################################################################################################

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"