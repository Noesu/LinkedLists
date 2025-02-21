from typing import Tuple, Union

Cm = Union[int, float]

class Thing:
    def __init__(self, name: int, weight: float) -> None:
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name: int, weight: float, author: str, date: str) -> None:
        super().__init__(name, weight)
        self.author = author
        self.date = date

class Computer(Thing):
    def __init__(self, name: int, weight: float, memory: int, cpu: str) -> None:
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    Cm = Union[int, float]
    def __init__(self, name: int, weight: float, dims: Tuple[Cm, Cm, Cm]) -> None:
        super().__init__(name, weight)
        self.dims = dims

class Mercedes(Auto):
    def __init__(self, name: int, weight: float, dims: Tuple[Cm, Cm, Cm], model: str, old: int) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old

class Toyota(Auto):
    def __init__(self, name: int, weight: float, dims: Tuple[Cm, Cm, Cm], model: str, wheel: bool) -> None:
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel

