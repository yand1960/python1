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

print("==============")
# 3. Найти все слова-палиндромы (лаз-зал). Асимптотика лучше, чем 0(n2)
# for w1 in words:
#     for w2 in words:
#         if w1 == w2[::-1]:
#             print(w1, w2)

# reversed = []
# for w in words:
#     reversed.append(w[::-1])

# reversed = [w[::-1]  for w in words]
# print(set(words).intersection(set(reversed)))

# print(set(words).intersection(set([w[::-1]  for w in words])))

results =[ (word, word[::-1]) for word in set(words).intersection(set([w[::-1] for w in words]))]
print(results)