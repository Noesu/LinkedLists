CURRENT_OS = 'windows'   # 'windows', 'linux'

class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

# здесь объявляйте класс FileDialogFactory

class FileDialogFactory:
    def __new__(cls, *args):
        return WindowsFileDialog(*args) if CURRENT_OS == 'windows' else LinuxFileDialog(*args)

    def create_windows_filedialog(title, path, exts): pass

    def create_linux_filedialog(title, path, exts): pass