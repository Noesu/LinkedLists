from random import choice, randint


class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    def clean_coords(self):
        self.sp, self.ep = (0, 0), (0, 0)


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


elements = []
for i in range(217):
    coordinates = [randint(0, 100) for _ in range(4)]
    elements.append(choice([Line, Rect, Ellipse])(*coordinates))

for element in elements:
    if type(element) == Line:
        element.clean_coords()