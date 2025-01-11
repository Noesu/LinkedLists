class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        # self.tr.setdefault(eng, [])
        if rus not in self.tr.setdefault(eng, []):
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]


tr = Translator()

e_words = ["tree", "car", "car", "leaf", "river", "go", "go", "go", "milk"]
r_words = ["дерево", "машина", "автомобиль", "лист", "река", "идти", "ехать", "ходить", "молоко"]
for e, r in zip(e_words, r_words):
    tr.add(e, r)

tr.remove("car")
print(*tr.translate("go"))