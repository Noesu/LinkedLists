TYPE_OS = 1  # 1 - Windows; 2 - Linux


class OS:
    def __init__(self, name):
        self.name = name


class DialogWindows(OS):
    name_class = "DialogWindows"


class DialogLinux(OS):
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)
        else:
            obj = super().__new__(DialogLinux)
        obj.__init__(*args, **kwargs)
        return obj
