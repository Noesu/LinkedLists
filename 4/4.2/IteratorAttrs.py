from typing import Tuple

class IteratorAttrs:
    def __iter__(self):
        for attr in self.__dict__:
            yield attr, self.__dict__[attr]

    # def __iter__(self):
    #     return iter(self.__dict__.items())
    #
    # def __iter__(self):
    #     yield from self.__dict__.items()

class SmartPhone(IteratorAttrs):
    def __init__(self, model: str, size: Tuple[int, int], memory: int) -> None:
        self.model = model
        self.size = size
        self.memory = memory

