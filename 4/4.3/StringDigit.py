def validate(string):
    if not all(symbol.isdigit() for symbol in str(string)):
        raise ValueError("в строке должны быть только цифры")

class StringDigit(str):
    def __new__(cls, string):
        validate(string)
        return super().__new__(cls, string)

    def __add__(self, other):
        validate(other)
        return self.__class__(super().__add__(str(other)))

    def __radd__(self, other):
        validate(other)
        return self.__class__(str(other) + str(self))

########################################################################################################################

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError