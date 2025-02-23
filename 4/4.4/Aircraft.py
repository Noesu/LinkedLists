from typing import Union

PosNum = Union[int, float]

class Aircraft:
    def __init__(self, model: str, mass: PosNum, speed: PosNum, top: PosNum):
        self._validate_model(model)
        self._validate_posnum(mass)
        self._validate_posnum(speed)
        self._validate_posnum(top)

        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @classmethod
    def _validate_model(cls, model):
        if type(model) is not str:
            raise TypeError('неверный тип аргумента')

    @classmethod
    def _validate_posnum(cls, unit):
        if type(unit) not in (int, float) or unit <= 0:
            raise TypeError('неверный тип аргумента')

    @classmethod
    def _validate_weapons(cls, weapons):
        pass

    @classmethod
    def _validate_chairs(cls, chairs):
        pass

class PassengerAircraft(Aircraft):
    def __init__(self, model: str, mass: PosNum, speed: PosNum, top: PosNum, chairs: PosNum):
        super().__init__(model, mass, speed, top)
        super()._validate_posnum(chairs)
        self._validate_chairs(chairs)
        self._chairs = chairs

    @classmethod
    def _validate_chairs(cls, chairs):
        if type(chairs) is not int:
            raise TypeError('неверный тип аргумента')

class WarPlane(Aircraft):
    def __init__(self, model: str, mass: PosNum, speed: PosNum, top: PosNum, weapons: dict):
        super().__init__(model, mass, speed, top)
        self._validate_weapons(weapons)
        self._weapons = weapons

    @classmethod
    def _validate_weapons(cls, weapons):
        if type(weapons) is not dict:
            raise TypeError('неверный тип аргумента')
        for key, value in weapons.items():
            if type(key) is not str or type(value) is not int:
                raise TypeError('неверный тип аргумента')

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

########################################################################################################################



