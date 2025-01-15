from itertools import count
from typing import List, Union

class Product:
    unique_id: count = count()

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]) -> None:
        self.id = self.get_next_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key: str, value: Union[str, float, int]) -> None:
        if key == "name" and isinstance(value, str):
            object.__setattr__(self, key, value)
        elif key in ("weight", "price", "id") and isinstance(value, (float, int)) and 0 <= value:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item: str) -> None:
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)

    @classmethod
    def get_next_id(cls) -> int:
        return next(cls.unique_id)

class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: List[Product] = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")




