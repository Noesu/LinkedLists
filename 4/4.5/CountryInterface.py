from abc import ABC, abstractmethod
from typing import Union

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self) -> str: pass

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None: pass

    @property
    @abstractmethod
    def population(self) -> int: pass

    @population.setter
    @abstractmethod
    def population(self, value: int) -> None: pass

    @property
    @abstractmethod
    def square(self) -> Union[int, float]: pass

    @square.setter
    @abstractmethod
    def square(self, value: Union[int, float]) -> None: pass

    @abstractmethod
    def get_info(self) -> str: pass

class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: Union[int, float]) -> None:
        self.name = name
        self.population = population
        self.square = square

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if type(value) is not str:
            raise ValueError
        self._name = value

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, value: int) -> None:
        if type(value) is not int or value <= 0:
            raise ValueError
        self._population = value

    @property
    def square(self) -> Union[int, float]:
        return self._square

    @square.setter
    def square(self, value: Union[int, float]) -> None:
        if type(value) not in (int, float) or value <= 0:
            raise ValueError
        self._square = value

    def get_info(self) -> str:
        return f'{self.name}: {self.square}, {self.population}'

########################################################################################################################

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
c = country.get_info().strip()
print(c)