from typing import Any, Callable, Union

Kg = Union[int, float]

class Thing:
    def __init__(self, n: str, w: Kg) -> None:
        self.name = n
        self.weight = w

def validate_weight(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self: "Bag", *args: Any, **kwargs: Any) -> Any:
        if isinstance(args[0], Thing):
            thing = args[0]
            weight_change = thing.weight
        else:
            thing = args[1]
            weight_change = thing.weight - self.inventory[0].weight
        actual_weight = sum(item.weight for item in self.inventory)
        if actual_weight + weight_change > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        return func(self, *args, **kwargs)
    return wrapper

def validate_index(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(self, indx: int, *args: Any, **kwargs: Any) -> Any:
        if indx >= len(self):
            raise IndexError('неверный индекс')
        return func(self, indx, *args, **kwargs)
    return wrapper


class Bag:
    def __init__(self, mw: Kg) -> None:
        self.max_weight = mw
        self.inventory = []

    @validate_index
    def __getitem__(self, indx: int) -> Thing:
        return self.inventory[indx]

    @validate_weight
    @validate_index
    def __setitem__(self, indx: int, item: Thing) -> None:
        self.inventory[indx] = item

    @validate_index
    def __delitem__(self, indx: int) -> None:
        del self.inventory[indx]

    def __len__(self) -> int:
        return len(self.inventory)

    @validate_weight
    def add_thing(self, thing: Thing) -> None:
        self.inventory.append(thing)

########################################################################################################################

# b = Bag(700)
# b.add_thing(Thing('книга', 100))
# b.add_thing(Thing('носки', 200))
#
# try:
#     b.add_thing(Thing('рубашка', 500))
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# assert b[0].name == 'книга' and b[
#     0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"
#
# t = Thing('Python', 20)
# b[1] = t
# assert b[1].name == 'Python' and b[
#     1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"
#
# del b[0]
# assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"
#
# try:
#     t = b[2]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
