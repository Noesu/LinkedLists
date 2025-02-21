from collections import Counter
from typing import List, Optional, Union

class Thing:
    def __init__(self, name: str, mass: Union[int, float]):
        self.mass = float(mass)
        self.name = name

    def __eq__(self, other: "Thing") -> bool:
        return self.name.lower() == other.name.lower() and self.mass == other.mass

class Box:
    def __init__(self):
        self.things: List[Optional[Thing]] = []

    def __eq__(self, other: "Box") -> bool:
        return Counter((t.name.lower(), t.mass) for t in self.things) == Counter((o.name.lower(), o.mass) for o in other.things)

    def add_thing(self, obj: Thing) -> None:
        self.things.append(obj)

    def get_things(self) -> List[Optional[Thing]]:
        return self.things

########################################################################################################################

b1 = Box()
assert b1.get_things() == [], "Список предметов при создании должен быть пустой"

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

assert len(b1.get_things()) == 3, "Функция добавление предметов в ящик реализована неверно"

b2 = Box()
th1 = Thing('тряпка', 200)
th2 = Thing('тряпка', 200)
assert th1 == th2, "Сравнение предметов реализовано некорректно"
th3_a = Thing('швабра', 300)
th3_b = Thing('швабра_1', 300)
th3_c = Thing('швабра', 200)
assert th3_a != th3_b or th3_b != th3_c, "Сравнение предметов реализовано некорректно"

b2.add_thing(th1)
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

assert b1 == b2, "Сравнение ящиков реализовано некорректно"
b2.add_thing(Thing('доска', 2000))
assert len(b2.get_things()) == 4, "Функция добавление предметов в ящик реализована неверно"
assert b1 != b2, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"

c1 = Box()
c1.add_thing(Thing('мел', 100))
c1.add_thing(Thing('Тряпка', 200))
c1.add_thing(Thing('Тряпка', 200))
c1.add_thing(Thing('доска', 2000))
c2 = Box()
c2.add_thing(Thing('тряпка', 200))
c2.add_thing(Thing('Мел', 100))
c2.add_thing(Thing('доска', 2000))
c2.add_thing(Thing('доска', 2000))
assert c1 != c2, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"

c3 = Box()
c3.add_thing(Thing('мел', 100))
c3.add_thing(Thing('Тряпка', 200))
c3.add_thing(Thing('доска', 2000))
c4 = Box()
c4.add_thing(Thing('тряпка', 200))
c4.add_thing(Thing('Мел', 100))
c4.add_thing(Thing('доска', 2000))
c4.add_thing(Thing('Указка', 200))
assert c3 != c4, "Сравнение ящиков реализовано некорректно, для каждого объекта класса Thing одного ящика можно найти ровно один равный объект из второго ящика"

