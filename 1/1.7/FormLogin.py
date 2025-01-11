from string import ascii_lowercase, digits

class Input:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if not self.check_name(name):
            raise ValueError("некорректное поле name")
        self.name = name
        self.size = size

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) < 50 and all(ltr in cls.CHARS_CORRECT for ltr in name):
            return True
        return False

    def get_html(self):
        p_class = "login" if isinstance(self, TextInput) else "password"
        return f"<p class='{p_class}'>{self.name}: <input type='text' size={self.size} />"

class TextInput(Input): pass
class PasswordInput(Input): pass


class FormLogin:
    def __init__(self, lgn: TextInput, psw: PasswordInput):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)