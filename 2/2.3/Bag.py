from typing import List

class Thing:
    def __init__(self, name: str, weight: int) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things: List[Thing] = []

    @property
    def things(self) -> List[Thing]:
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, thing: Thing) -> None:
        self.__things.remove(thing)

    def get_total_weight(self) -> int:
        return sum(thing.weight for thing in self.__things)


########################################################################################################################

bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")



