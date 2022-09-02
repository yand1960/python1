# "приватный доступ" к членам класса и понятие "свойство класса"

# "Явский стиль" доступа к приватному полю
class A:

    def __init__(self, value: int):
        # self._value = value
        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value > 100:
            self._value = value
        else:
            raise ValueError("Допустимы только числа больше 100")

# a = A(123)
# a.value = 777
# a._value = 999
# print(a._value)
# print(a.get_value())
# a.set_value(99) # error!

# Явное определение свойства у класса с использованием функции property
class B:

    def __init__(self, value: int):
        self.value = value
        # self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if value > 100:
            self._value = value
        else:
            raise ValueError("Допустимы только числа больше 100")

    value = property(get_value, set_value)

# b = B(666)
# print(b.value)
# b.value = 777
# print(b.value)
# b.value = 77 # error!

# Явное определение свойства у класса с использованием декоратора property
class C:

    def __init__(self, value: int):
        self.value = value
        # self.set_value(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value > 100:
            self._value = value
        else:
            raise ValueError("Допустимы только числа больше 100")


c = C(123)
print(c.value)
c.value = 666
print(c.value)
c.value = 77 # error!
