from typing import Optional, Union


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs) -> None:
        pass

    @classmethod
    def register(cls, money: "Money") -> None:
        money.cb = cls


class Money:
    Amount = Union[int, float]
    cur_name = None

    def __init__(self, money: Amount = 0, cb: Optional[CentralBank] = None) -> None:
        self.volume = money
        self.cb = cb

    def __lt__(self, other: "Money") -> bool:
        self.check_cb_registration()
        rates = self.cb.rates
        return self.volume / rates.get(self.cur_name) < other.volume / rates.get(other.cur_name)

    def __le__(self, other: "Money") -> bool:
        self.check_cb_registration()
        rates = self.cb.rates
        return self.volume / rates.get(self.cur_name) <= other.volume / rates.get(other.cur_name)

    def __eq__(self, other: "Money") -> bool:
        self.check_cb_registration()
        rates = self.cb.rates
        return 0.99 <= (self.volume / rates.get(self.cur_name)) / (other.volume / rates.get(other.cur_name)) <= 1.1

    def check_cb_registration(self) -> None:
        if not self.cb:
            raise ValueError("Неизвестен курс валют.")

    @property
    def volume(self) -> Amount:
        return self.__volume

    @volume.setter
    def volume(self, money: Amount) -> None:
        self.__volume = money

    @property
    def cb(self) -> CentralBank:
        return self.__cb

    @cb.setter
    def cb(self, value: CentralBank) -> None:
        self.__cb = value


class MoneyR(Money): cur_name = "rub"
class MoneyD(Money): cur_name = "dollar"
class MoneyE(Money): cur_name = "euro"


########################################################################################################################

cb = CentralBank
assert cb is not None, "Объекты класса CentralBank создаваться не должны, должно просто возвращаться значение None "

r = MoneyR(45_000)
assert r.volume == 45_000, "Неверно присваивается значение"
assert r.cb is None, "Кошелёк при создании должен быть не зарегистрирован"
CentralBank.register(r)
assert r.cb is not None, "Кошелёк должен быть уже зарегистрирован"

r1 = MoneyR(45_000.0005)
CentralBank.register(r1)
assert r == r1, "Сравнение кошельков вернуло False, при значениях 45_000 и 45_000.0005"

d = MoneyD(45_000 / cb.rates['rub'])
e = MoneyE(45_000 / (cb.rates['rub'] * cb.rates['euro']))

try:
    d == r
except ValueError as err:
    assert err != "Неизвестен курс валют.", "Не генерируется исключение для незарегистрированного кошелька"

CentralBank.register(d)
CentralBank.register(e)

assert r == d, "Неверно реализованно сравнение кошельков"
assert e == d, "Неверно реализованно сравнение кошельков"
assert r == e, "Неверно реализованно сравнение кошельков"

e2 = e = MoneyE(40_000 / (cb.rates['rub'] * cb.rates['euro']))
CentralBank.register(e2)
assert e2 < r, "Неверно реализованно сравнение кошельков"