class WindowDlg:
    def __init__(self, title: str, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        if 0 < width < 10000:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        if 0 < height < 10000:
            self.__height = height
            self.show()



wnd = ("Window title", 100, 200)
wnd.w
print(wnd.sh)
