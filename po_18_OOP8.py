# полимофизм и утиная типизация
# абстрактные классы и интерфейсы - как питон без них обходится

class Animal:
    def __init__(self):
        self.voice = None
        raise NotImplementedError("Это абстрактный класс")

class Cat(Animal):
    def __init__(self, voice = "Meaow"):
        self.voice = voice

class Dog(Animal):
    def __init__(self, voice = "Hab"):
        self.voice = voice

cat = Cat()
# print(cat.voice)
dog = Dog()
# print(dog.voice)

# animal = Animal() # error

def call(animal: Animal):
    print("Come to me!")
    print(animal.voice)

call(cat)
call(dog)
# call(123)
call(animal)