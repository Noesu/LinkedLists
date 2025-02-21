class Ellipse:
    def __init__(self, *coords):
        if coords:
            self.x1, self.y1, self.x2, self.y2 = coords

    def __bool__(self):
        return bool(self.__dict__)

    def get_coords(self):
        if bool(self):
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')

lst_geom = [Ellipse(), Ellipse()]
lst_geom.extend([Ellipse(1,2,3,4), Ellipse(5,6,7,8)])
for elem in lst_geom:
    if bool(elem):
        elem.get_coords()