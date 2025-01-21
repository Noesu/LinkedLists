import time
from typing import Generator, Optional, Union


class Cartridge:
    def __setattr__(self, key: str, value: float) -> None:
        if not hasattr(self, "date"):
            object.__setattr__(self, key, value)

class Mechanical(Cartridge):
    def __init__(self, date: float) -> None:
        self.date = date

class Aragon(Cartridge):
    def __init__(self, date: float) -> None:
        self.date = date

class Calcium(Cartridge):
    def __init__(self, date: float) -> None:
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self) -> None:
        self.slots: dict[int, Optional[Union[Mechanical, Aragon, Calcium]]] = {
            1: None,  # Слот для Mechanical
            2: None,  # Слот для Aragon
            3: None   # Слот для Calcium
        }

    def add_filter(self, slot_num: int, filter: Optional[Union[Mechanical, Aragon, Calcium]]) -> None:
        if not self.slots.get(slot_num):
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num: int) -> None:
        if self.slots.get(slot_num):
            self.slots[slot_num] = None

    def get_filters(self) -> Generator[Optional[Union[Mechanical, Aragon, Calcium, bool]]]:
        return (self.slots.get(key) for key in self.slots.keys() if not None)

    def water_on(self) -> bool:
        for installed_cartridge in self.slots.values():
            if not installed_cartridge:
                return False
            elif installed_cartridge.date + self.MAX_DATE_FILTER < time.time():
                return False
        return True


########################################################################################################################

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"