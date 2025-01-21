class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
        return True

class LengthValidator:
    def __init__(self, min_length: int, max_length: int) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string: str, *args, **kwargs) -> bool:
        return self.min_length <= len(string) <= self.max_length

class CharsValidator:
    def __init__(self, chars: str) -> None:
        self.chars = chars

    def __call__(self, string: str, *args, **kwargs) -> bool:
        return set(string).issubset(self.chars)




########################################################################################################################

from string import ascii_lowercase, digits

lg = LoginForm("Вход на сайт", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")

lv = LengthValidator(min_length, max_length) # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator(chars) # chars - строка из допустимых символов

res = lv(string)
res = cv(string)