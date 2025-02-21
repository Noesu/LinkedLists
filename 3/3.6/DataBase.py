import sys

class Record:
    _id = 1

    def __init__(self, fio: str, descr: str, old: int) -> None:
        self.pk = type(self)._id
        self.fio = fio
        self.descr = descr
        self.old = old
        type(self)._id += 1

    def __hash__(self) -> int:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: "Record") -> bool:
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path: str) -> None:
        self.path = path
        self.dict_db = dict()

    def write(self, record: Record) -> None:
        # self.dict_db.setdefault(record, []).extend([key for key in self.dict_db.keys() if key == record])
        self.dict_db.setdefault(record, []).append(record)
        # for key in self.dict_db:
        #     if key == record:
        #         self.dict_db[key].append(record)
        #         return
        # self.dict_db[record] = [record]

    def read(self, pk: int) -> Record:
        for records in self.dict_db.values():
            for record in records:
                if record.pk == pk:
                    return record

lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('хзчтоизачем')
for line in lst_in:
    name, descr, age = line.split(';')
    db.write(Record(name, descr.strip(), int(age.strip())))

########################################################################################################################

d = tuple(db.dict_db.values())[0][0]
assert type(d.descr) == str and type(d.fio) == str and type(
    d.old) == int, "значениями словаря должен быть список из объектов класса Rect с набором атрибутов: descr (строка), fio (строка), old (целое число)"

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"