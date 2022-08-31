# Практический пример класса: инкапсулирует
# 1. извлечение списка слов из файла
# 2. Статистику частоты букв в словаре
# 3. Статистика по длинам слов

class Vocabulary:

    def __init__(self, path: str, encoding: str = "utf-8", separator: str = "\n"):
        with open(path, encoding=encoding) as f:
            text = f.read()
        self.words = text.split(separator)

    def statistics_letters(self):
        text = str().join(self.words)
        letters = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
        results = {}
        for letter in letters:
            results[letter] = text.count(letter)
        return results

    def statistics_length(self):
        results = [0 for i in range(1,30)]
        for w in self.words:
            results[len(w)] += 1
        return results


words = Vocabulary("data/RusDictionary.txt").words
vocab1 = Vocabulary("data/RusDictionary.txt")
vocab2 = Vocabulary("data/RusDictionary.txt")
# vocab1.words = ["а", "б"]

print(vocab1.statistics_letters())
print(vocab1.statistics_length())
