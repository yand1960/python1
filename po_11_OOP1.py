# Это не совсем типичный класс. В других плтаформах такой класс
# назвали бы статическим. Для него бессмысленнно понятие объекта.
class MyGeometry:

    # Это называется "поле класса". Не совсем точно: "свойство класса"
    non_euqluid = 1.0

    # Это называется "метод класса"
    def hypot(a, b):
        result = ((a * a + b * b) ** 0.5) * MyGeometry.non_euqluid
        return result

    def square(a, b):
        return a * b / 2 * MyGeometry.non_euqluid


# По Эвклиду
print(MyGeometry.hypot(3, 4))

# По Лобачевскому
MyGeometry.non_euqluid = 0.9
print(MyGeometry.hypot(3,4), MyGeometry.square(3, 4))

# По Гауссу
MyGeometry.non_euqluid = 1.1
print(MyGeometry.hypot(3, 4), MyGeometry.square(3, 4))