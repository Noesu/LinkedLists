import sys
from typing import Union

class ShopItem:
    def __init__(self, n, w, p):
        self.price = p
        self.weight = w
        self.name = n

    def __hash__(self):
        return hash((self.name.lower(), self.price, self.weight))

    def __eq__(self, other):
        return all((self.name.lower() == other.name.lower(), self.price == other.price, self.weight == other.weight))


lst_in = list(map(str.strip, sys.stdin.readlines()))

shop_items = dict()
for item in lst_in:
    name, details = item.split(':')
    weight, price = map(float, details.split())
    x = ShopItem(name, weight, price)
    if x in shop_items:
        shop_items[x][1] += 1
    else:
        shop_items[x] = [x, 1]


########################################################################################################################



it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"

