class Morph:
    def __init__(self, *words: str):
        self.words = [word for word in words]

    def __eq__(self, other: str):
        return other.lower() in self.words

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def get_words(self):
        return tuple(self.words)

dict_words = [['связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'],
              ['формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам',
'формулами', 'формулах'],
              ['вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'],
              ['эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'],
              ['день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях']]
dict_words = [Morph(*i) for i in dict_words ]

# text = input()
text = "Мы будем устанавливать связь завтра днем."
text = text[:-1]
words_count = 0
for word in text.split():
    for dict_word in dict_words:
        if word.lower() == dict_word:
            print(word)
            words_count += 1
print(words_count)


########################################################################################################################

mw = dict_words[0]
assert mw.get_words() == ('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'), "метод get_words вернул неверные данные"
mw1 = Morph('свет', 'светом')
mw1.add_word('свете')
mw1.add_word('свете')
mw1.add_word('свет')
assert mw1.get_words() == ('свет', 'светом', 'свете'), "метод get_words вернул неверные данные"
assert mw1 == 'свете', "метод == работает некорректно"
assert mw1 != 'света', "метод != работает некорректно"
assert 'сВете' == mw1, "метод == работает некорректно"
assert 'света' != mw1, "метод != работает некорректно"