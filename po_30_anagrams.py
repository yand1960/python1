with open("data/RusDictionary.txt", encoding="utf-8") as f:
    text = f.read()

words = text.split("\n")
# print(words[0:100])

# найти все "гнезда" слов, которые можно получить перестановками букв

w1 = "пост"
w2 = "стоп"

def hash(word):
    return str.join("", sorted(word))

# Наивный алгоритм
# for w1 in words:
#     for w2 in words:
#         if hash(w1) == hash(w2) and w1 != w2:
#             print(w1, w2)

#  Вариант 1
# hash_word = []
# for w in words:
#     hash_word.append([hash(w), w])
#
# sorted_hash_word = sorted(hash_word, key=lambda hw: hw[0])
# # print(sorted_hash_word[0:100])
# for i in range(1, len(sorted_hash_word)):
#     if sorted_hash_word[i][0] == sorted_hash_word[i - 1][0]:
#         print(sorted_hash_word[i - 1][1], sorted_hash_word[i][1])

# Вариант 2
hash_words = {}
for w in words:
    hash_words[hash(w)] = []

for w in words:
    hash_words[hash(w)].append(w)

for anagrams in hash_words.values():
    if len(anagrams) > 1:
        print(anagrams)
