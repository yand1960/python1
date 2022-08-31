# полимофизм и утиная типизация

class Cat:
    def __init__(self, voice = "Meaow"):
        self.voice = voice

class Dog:
    def __init__(self, voice = "Hab"):
        self.voice = voice

cat = Cat()
# print(cat.voice)
dog = Dog()
# print(dog.voice)

def call(animal):
    print("Come to me!")
    print(animal.voice)

call(cat)
call(dog)
# call(123)