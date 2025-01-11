from random import randint, sample
from string import ascii_letters, digits


email_chars = ascii_letters + digits + "_."

class EmailValidator:
    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def get_random_email(cls):
        return ''.join(sample(email_chars, randint(1, 100))) + "@gmail.com"

    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email): return False
        if not email.count("@") == 1: return False
        if not set(email).issubset(email_chars + "@"): return False
        username, domain = email.split("@")
        if len(username) > 100: return False
        if len(domain) > 50: return False
        if domain.count(".") < 1: return False
        if ".." in email: return False
        if not "." in domain: return False
        return True

    @staticmethod
    def __is_email_str(email):
        return True if isinstance(email, str) else False

######################################

print(EmailValidator.check_email("sc_lib@list.ru")) # True
print(EmailValidator.check_email("sc_lib@list_ru")) # False