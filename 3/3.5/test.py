a = "Я к вам пишу – чего же боле?"
b = a.translate(str.maketrans("", "", "–?!,.;")).split()
print(b)