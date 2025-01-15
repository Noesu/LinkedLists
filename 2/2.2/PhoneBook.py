from typing import List

class PhoneNumber:
    def __init__(self, number: int, fio: str) -> None:
        self.number = number
        self.fio = fio

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int) -> None:
        if isinstance(number, int) and 9_999_999_999 < number <= 99_999_999_999:
            self.__number = number
        elif isinstance(number, str) and number.isdigit() and len(number) == 11:
            self.__number = int(number)
        else:
            print("Wrong phone number")

    @property
    def fio(self) -> str:
        return self.__fio

    @fio.setter
    def fio(self, fio: str) -> None:
        if fio:
            self.__fio = str(fio)


class PhoneBook:
    def __init__(self) -> None:
        self.phones: List[PhoneNumber] = []

    def add_phone(self, phone: PhoneNumber) -> None:
        self.phones.append(phone)

    def remove_phone(self, indx: int) -> None:
        if 0 <= indx < len(self.phones):
            self.phones.pop(indx)

    def get_phone_list(self) -> List[PhoneNumber]:
        return self.phones


########################################################################################################################

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)