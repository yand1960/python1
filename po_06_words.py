with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()

words = text.split("\n")
#print(words[0:200])

# 1. Найти слова, которые заканчиваются на цо
# 2. Найти все слова-перевертыши (боб, казак и т.д.)
# 3. Найти все слова-палиндромы (лаз-зал). Асимптотика лучше, чем 0(n2)

pattern = "цо"
for w in words:
    if w[-2:] == pattern:
        print(w)