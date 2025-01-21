from random import choices, randint

class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs) -> str:
        return "".join(choices(self.psw_chars, k=randint(self.min_length, self.max_length)))

rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for _ in range(3)]


########################################################################################################################

print(lst_pass)
