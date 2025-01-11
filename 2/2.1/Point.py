class Point:
    def __init__(self, x, y):
        self.__x, self.__y = x, y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            self.__sp = Point(*args[:2])
            self.__ep = Point(*args[2:])
        else:
            self.__sp = args[0]
            self.__ep = args[1]

    def __str__(self):
        return f"Прямоугольник с координатами: {self.__sp} {self.__ep}"

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(self)


rect = Rectangle(Point(0, 0), Point(20, 34))
rect.draw()
