# Это типичный класс. Для него существенно понятие объекта.
class MyGeometry:

    # Это называется "конструктор класса"
    def __init__(self, non_euguid = 1.0):
        # Это называется "поле класса".
        # Не совсем точно: "свойство класса"
        # В данном случае поле относится не к классу в целом,
        # а к экземпляру этого класса (о чем гооврит self)
        self.non_euqluid = non_euguid

    # Это называется "метод класса".
    # Слово self указывает, что метод относится к объекту этого калсса
    def hypot(self, a, b):
        # self.bubu = 123
        result = ((a * a + b * b) ** 0.5) * self.non_euqluid
        return result

    def square(self, a, b):
        return a * b / 2 * self.non_euqluid


# Создаем экземпляры класса:
geometry1 = MyGeometry()
# geometry2 = MyGeometry()
# geometry2.non_euqluid = 0.9
geometry2 = MyGeometry(0.9)
# geometry3 = MyGeometry()
# geometry3.non_euqluid = 1.1
geometry3 = MyGeometry(1.1)

# По Эвклиду
print(geometry1.hypot(3, 4))
print(geometry2.hypot(4, 5))

# По Лобачевскому
print(geometry2.hypot(3, 4), geometry2.square(3, 4))

# По Гауссу
print(geometry3.hypot(3, 4), geometry3.square(3, 4))

#  И далее куча вычислений с тремя нащшими объкетами

