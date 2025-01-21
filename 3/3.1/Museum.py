from typing import List, Union

class Item:
    attrs = {"name": str, "descr": str}
    def __init__(self, name: str, descr: str) -> None:
        self.name = name
        self.descr = descr

    def __setattr__(self, key: str, value: str) -> None:
        attr_type = self.attrs.get(key)
        if not isinstance(value, attr_type):
            raise ValueError(f"Для атрибута '{key}' значение {value} не соответствует значению {attr_type}.")
        super().__setattr__(key, value)

class Picture(Item):
    attrs = {**Item.attrs, "author": str}
    def __init__(self, name: str, author: str, descr: str):
        super().__init__(name, descr)
        self.author = author

class Mummies(Item):
    attrs = {**Item.attrs, "location": str}
    def __init__(self, name: str, location: str, descr: str):
        super().__init__(name, descr)
        self.location = location

class Papyri(Item):
    attrs = {**Item.attrs, "date": str}
    def __init__(self, name: str, date: str, descr: str):
        super().__init__(name, descr)
        self.date = date

class Museum:
    def __init__(self, name: str) -> None:
        self.name = name
        self.exhibits: List[Union[Picture, Mummies, Papyri]] = []

    def add_exhibit(self, obj: Union[Picture, Mummies, Papyri]) -> None:
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: Union[Picture, Mummies, Papyri]) -> None:
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int) -> str:
        item = self.exhibits[indx]
        return f"Описание экспоната {item.name}: {item.descr}"

########################################################################################################################

# TEST-TASK___________________________________
mus = Museum("Эрмитаж")
assert type(mus.name) is str, "название должно быть строкой"
assert mus.exhibits == [], "exhibits должен быть списком"
assert hasattr(mus, "add_exhibit"), "метод не объявлен"
assert hasattr(mus, "remove_exhibit"), "метод не объявлен"
assert hasattr(mus, "get_info_exhibit"), "метод не объявлен"

pic = Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
              "Вдохновляющая, устрашающая, волнующая картина")
assert 'name' in pic.__dict__.keys() and 'descr' in pic.__dict__.keys() and 'author' in pic.__dict__.keys(), "ошибка в локальных атрибутах"

mum = Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации")
assert 'name' in mum.__dict__.keys() and 'location' in mum.__dict__.keys() and 'descr' in mum.__dict__.keys(), "ошибка в локальных атрибутах"

p = Papyri("Ученья для, не злата ради",
           "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
assert 'name' in p.__dict__.keys() and 'date' in p.__dict__.keys() and 'descr' in p.__dict__.keys(), "ошибка в локальных атрибутах"
assert type(p.date) is str, "название должно быть строкой"


mus.add_exhibit(pic)
assert mus.exhibits[0] == pic and len(mus.exhibits) == 1, "некорректно отработал метод add_exhibit"

mus.remove_exhibit(pic)
assert len(mus.exhibits) == 0 and pic not in mus.exhibits, "некорректно отработал метод remove_exhibit"

mus.add_exhibit(p)
mus.add_exhibit(pic)
answ = mus.get_info_exhibit(0)
print(answ)
print(f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}")
assert answ == f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}", "некорректно отработал метод get_info_exhibit"
print("Правильный ответ.")