# Наследование

from po_13_OOP3 import Person

class Boss(Person):
     def scream(self):
         return f"Я - {self.last_name}! Всем работать!"


boss1 = Boss("Bill", "Gates", 1234567)
print(boss1)
print(boss1.scream())