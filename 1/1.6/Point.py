class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def clone(self):
        obj = super().__new__(Point)
        obj.__init__(self.x, self.y)
        return obj

    # def clone(self):
    #     return Point(self.x, self.y)

    # def clone(self):
    #     new_clone = super().__new__(type(self))
    #     new_clone.__dict__.update(self.__dict__)
    #     return new_clone

    # def clone(self):
    #     return type(self)(**self.__dict__)


pt = Point(1, 2)
pt_clone = pt.clone()