import sys

class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj

lst_in =  list(map(str.strip, sys.stdin.readlines()))
l = iter(lst_in)
node = head_obj = ListObject(next(l))

for line in l:
    next_node = ListObject(line)
    node.link(next_node)
    node = next_node




assert isinstance(head_obj, ListObject) and hasattr(ListObject, 'link')

lst_data = []
h = head_obj
while h:
    lst_data.append(h.data)
    h = h.next_obj

assert lst_in == lst_data, "данные в объектах ListObject не совпадают с прочитанными данными (списком lst_in)"


print(head_obj.data)