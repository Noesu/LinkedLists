class ItemAttrs(list):
    pass

class Point(ItemAttrs):
    def __init__(self, x, y):
        super().__init__((x, y))

########################################################################################################################

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10