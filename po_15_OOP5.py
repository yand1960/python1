# Наследование, проблемы динамического расширения
from po_13_OOP3 import Person


class Boss(Person):

    # расширение супер класса
    def scream(self):
         return f"Я - {self.last_name}! Всем работать!"

    # перекрытие метода класса-предка
    def __str__(self):
        return "I am boss!"


class Manager(Person):

    # По сути, __slots__ заменяет __dict__,
    # запрещая динамическое расширение класса.
    # Слоты наследника добавляются к слотам предка.
    # Это означает, что если  надо запретить динамическое расширение класса,
    # то __dict__ должен быть отменен также и у предка
    # и __dict__ при этом нельзя  добавлять к слотам
    __slots__ = "level"

    def __init__(self, first_name, last_name, salary, level):
        super().__init__(first_name, last_name, salary)
        self.level = level

    def __str__(self):
        return "Manager: " + super().__str__() + f" level {self.level}"

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name
        #return self.__dict__ == other.__dict__


# boss1 = Boss("Bill", "Gates", 1234567)
# print(boss1)
# print(boss1.scream())

manager1 = Manager("Bill", "Gates", 123456789, level=0)
print(manager1)
manager2 = Manager("Bill", "Gates", 123456789, level=0)
print(manager2 is manager1, manager2 == manager1)

class ControlledList(list):

    def append(self, value):
        if value % 2 == 1:
            super().append( value)
        else:
            raise ValueError("только нечетные числа допустимы")

    def __setitem__(self, key, value):
        if value % 2 == 1:
            super().__setitem__(key, value)
        else:
            raise ValueError("только нечетные числа допустимы")

list1 = ControlledList([])
list1.append(1)
list1.append(7)
print(list1)
list1[1] = 81
print(list1)

manager3 = Manager("A","B", 123, 80)
#manager3.mumu = "MUMU!"
print(manager3.first_name)
#print(manager3.mumu)

x = 8
# x.mumu = "mumu"

person1 = Person("A","B", 111)
#person1.mumu = "MUMU!"

