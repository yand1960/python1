import re

passport = "12 34 123456"

# try:
#     valid = True
#
#     if len(passport) != 12:
#         valid = False
#
#     if passport[2] != " " or passport[5] != " ":
#         valid = False
#
#     for i in [0,1,3,4,6,7,8,9,10,11]:
#         if not (passport[i] >= "0" and passport[i] <= "9"):
#             valid = False
# except:
#     valid = False
#
# print(valid)

# \d - цифра
# ^ - начало текста, $ - конец текста
pattern = "^\d{2} \d{2} \d{6}$"
result = re.match(pattern, passport)

print(not (result is None))

text = """
Мама мыла раму.
Тетя Оля поехала в Турцию.
Тетя Даша тащила шпалу.
Тетя Глаша мыла пол.
Пете 5.5 лет.
Андрею 6,5 лет.
Моя тётя Вера мыла пол.
Дядя Вася тащил шпалу.
Маше 3 года.
"""

# Как зовут тетю, которая мыла пол
# \S - не пробельные символы, \s - пробельные символы
# (...) - группа, которая нас интересует
# + - предыдущий символ в любом количестве от 1
# [Тт] - Т или t
# {0,1} - 0 или 1 раз
pattern = "[Тт][её]тя (\S+) мыла пол"
results = re.findall(pattern, text)
print(results)

# Как зовут тех, которые тащил шпалу
pattern = "(\S+) тащила{0,1} шпалу"
results = re.findall(pattern, text)
print(results)

# Найти все числа (9:40)
pattern = "\d+[\.,\s]\d{0,}"
results = re.findall(pattern, text)
print(results)


