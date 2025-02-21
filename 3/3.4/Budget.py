from typing import List, Optional, Union

class Item:
    def __init__(self, name: str, money: Union[int, float]) -> None:
        self.money = money
        self.name = name

    def __add__(self, other: "Item") -> Union[int, float]:
        return self.money + other.money

    def __radd__(self, other: Union[int, float]) -> Union[int, float]:
        return self.money + other

class Budget:
    def __init__(self) -> None:
        self.items: list[Optional[Item]] = []

    def add_item(self, it: Item) -> None:
        self.items.append(it)

    def remove_item(self, indx: int) -> None:
        self.items.pop(indx)

    def get_items(self) -> List[Optional[Item]]:
        return self.items


########################################################################################################################

my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x