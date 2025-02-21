from typing import Any, Iterable, Union

class ListInteger(list):
    def __init__(self, values: Iterable[Any]) -> None:
        for value in values:
            self.__validate(value)
        super().__init__(values)

    def __setitem__(self, key: Union[int, slice], value: Any) -> None:
        self.__validate(value)
        super().__setitem__(key, value)

    @staticmethod
    def __validate(value: Any) -> None:
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, value: Any) -> None:
        self.__validate(value)
        super().append(value)


########################################################################################################################

s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError