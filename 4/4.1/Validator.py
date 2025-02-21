from typing import Optional, Union

class Validator:
    data_type: Optional[type] = None
    def __init__(self, minv:Union[int, float], maxv:Union[int, float]) -> None:
        self.min_value = minv
        self.max_value = maxv

    def __call__(self, data: Union[int, float]) -> Union[int, float]:
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return data

    def _is_valid(self, data: Union[int, float]) -> bool:
        return type(data) is self.data_type and self.min_value <= data <= self.max_value

class IntegerValidator(Validator):
    data_type: Optional[type] = int

class FloatValidator(Validator):
    data_type: Optional[type] = float

########################################################################################################################

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(10)    # исключение ValueError
