with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()

words = text.split("\n")
# print(words[0:100])

# найти все "гнезда" слов, которые можно получить перестановками букв