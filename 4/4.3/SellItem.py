from typing import List, Optional, Union

Price = Union[int, float]

class SellItem:
    def __init__(self, name:str, price: Price) -> None:
        self.name = name
        self.price = price

class House(SellItem):
    def __init__(self, name:str, price: Price, material: str, square: Union[int, float]) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square

class Flat(SellItem):
    def __init__(self, name:str, price: Price, size: Union[int, float], rooms: int) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms

class Land(SellItem):
    def __init__(self, name:str, price: Price, square: Union[int, float]) -> None:
        super().__init__(name, price)
        self.square = square

class Agency:
    def __init__(self, name: str) -> None:
        self.name = name
        self.objects: List[Optional[Union[House, Flat, Land]]] = []

    def add_object(self, obj: Union[House, Flat, Land]) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: Union[House, Flat, Land]) -> None:
        self.objects.remove(obj)

    def get_objects(self) -> List[Optional[Union[House, Flat, Land]]]:
        return self.objects
