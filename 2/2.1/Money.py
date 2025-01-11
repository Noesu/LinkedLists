class Money:
    def __init__(self, amount: int):
        if self.__check_money(amount):
            self.__money = amount

    def set_money(self, amount: int):
        if self.__check_money(amount):
            self.__money = amount

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

    @classmethod
    def __check_money(cls, amount: int) -> bool:
        return isinstance(amount, int) and amount >= 0

#################

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

print(m1, m2)