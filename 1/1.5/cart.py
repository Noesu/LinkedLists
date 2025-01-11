class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price}'


class Table(Product): pass
class TV(Product): pass
class Notebook(Product): pass
class Cup(Product): pass


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, *gd: Product):
        self.goods.extend(gd)

    def remove(self, indx: int):
        self.goods.pop(indx)

    def get_list(self):
        return [str(product) for product in self.goods]


cart = Cart()
cart.add(
    TV("Sony", 500),
    TV("Philips", 400),
    Table("Round", 100),
    Notebook("Apple", 899.99),
    Notebook("Lenovo", 600),
    Cup("Black", 30)
)
print(cart.get_list())
