class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_attrs = len(kwargs)
        # self.__attrs = tuple(self.__dict__.keys())
        self.__attrs = tuple(kwargs.keys())

    def __check_index(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx <= self.__total_attrs):
            raise IndexError('неверный индекс поля')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.__attrs[key], value)

########################################################################################################################

r = Record(pk=1, title="Python ООП", author="Балакирев")
r[0] = 2
r[1] = 'Супер курс по ООП'
r[2] = 'Балакирев С.М.'
print(r[1])
print(r[-1])
r[-1] = 0
print(r[1])