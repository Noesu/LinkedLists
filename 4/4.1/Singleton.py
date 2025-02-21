class Singleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name
