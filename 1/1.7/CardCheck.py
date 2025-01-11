from string import ascii_uppercase, digits

class CardCheck:
    CHARS_FOR_NAME = set(ascii_uppercase + digits)

    @staticmethod
    def check_card_number(number: str) -> bool:
        blocks = number.split('-')
        return (
                len(blocks) == 4 and
                all(len(block) == 4 and block.isdigit() for block in blocks)
        )

    @classmethod
    def check_name(cls, name: str) -> bool:
        name_parts = name.split()
        if len(name_parts) != 2:
            return False
        for part in name_parts:
            if not set(part).issubset(cls.CHARS_FOR_NAME):
                return False
        return True


print(CardCheck.check_name("SERGEI BALAKIREV"))

    