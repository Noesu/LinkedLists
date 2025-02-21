from typing import Union

class Body:
    def __init__(self, name: str, ro: Union[int, float], volume: Union[int, float]) -> None:
        self.mass = ro * volume

    def __gt__(self, other: Union["Body", int, float]) -> bool:
        if isinstance(other, Body):
            other = other.mass
        return self.mass > other

    def __lt__(self, other: Union["Body", int, float]) -> bool:
        if isinstance(other, Body):
            other = other.mass
        return self.mass < other

    def __eq__(self, other: Union["Body", int, float]) -> bool:
        if isinstance(other, Body):
            other = other.mass
        return self.mass == other


########################################################################################################################

body1 = Body("1", 10, 10)
body2 = Body("2", 15, 15)
print(body1 > body2)  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5)     # True, если масса тела body2 равна 5