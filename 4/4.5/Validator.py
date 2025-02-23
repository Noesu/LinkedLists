class Validator:
    def __call__(self, value: float) -> bool:
        return self._is_valid(value)

    def _is_valid(self, value: float) -> bool:
        raise NotImplementedError('в классе не переопределен метод _is_valid')

class FloatValidator(Validator):
    def __init__(self, min_value: float, max_value: float) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, value: float) -> bool:
        return type(value) is float and self.min_value <= value <= self.max_value

########################################################################################################################

float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])

