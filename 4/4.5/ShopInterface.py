from abc import ABC, abstractmethod
from typing import Union

class ShopInterface(ABC):
    @abstractmethod
    def get_id(self) -> None:
        raise NotImplementedError('в классе не переопределен метод get_id')

class ShopItem(ShopInterface):
    _id = 0

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]) -> None:
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = type(self)._id
        type(self)._id += 1

    def get_id(self) -> int:
        return self.__id
