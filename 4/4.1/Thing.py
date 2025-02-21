from itertools import count
from typing import Optional, Tuple

class Thing:
    _id = count()

    def __init__(
            self,
            name: str,
            price: float,
            weight: Optional[float] = None,
            dims: Optional[Tuple[float, float, float]] = None,
            memory: Optional[int] = None,
            frm: Optional[str] = None
    ) -> None:
        self.name: str = name
        self.price: float = price
        self.id: int = self.get_next_id()
        self.weight: Optional[float] = weight
        self.dims: Optional[Tuple[float, float, float]] = dims
        self.memory: Optional[int] = memory
        self.frm: Optional[str] = frm

    @classmethod
    def get_next_id(cls) -> int:
        return next(cls._id)

    def get_data(self) -> Tuple[
        int, str, float, Optional[float], Optional[Tuple[float, float, float]], Optional[int], Optional[str]]:
        return (
            self.id,
            self.name,
            self.price,
            self.weight,
            self.dims,
            self.memory,
            self.frm
        )

class Table(Thing):
    def __init__(self, name: str, price: float, weight: float, dims: Tuple[float, float, float]):
        super().__init__(name, price, weight=weight, dims=dims)

class ElBook(Thing):
    def __init__(self, name: str, price: float, memory: int, frm: str):
        super().__init__(name, price, memory=memory, frm=frm)

########################################################################################################################

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())