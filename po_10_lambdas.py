from typing import Callable

def f1(x):
    return 2 * x

print(f1(123))

#  функции можно епредавать в переменные
f2 = f1
print(f2(2))
f3 = f2
print(f3(3))

# Обобщенная функция - принимает в качестве аргумента другие функции
def f4(x: int, f: Callable[[int], int]) -> int:
    x +=1
    result = f(x)
    return result

print(f4(2, f2))

print(f4(f2(2), f3))

# Изобретение велосипеда: трансформация списка
data = [1, 2, 3, 4]

results = []
# for x in data:
#     results.append(x * x)
# print(results)
# print([x * x for x in data])
# def convert_to_square(data: list[int]) -> list[int]:
#     results = []
#     for x in data:
#         results.append(x * x)
#     return results
# print(convert_to_square(data))

def transform(data, convert_one):
    results = []
    for x in data:
        results.append(convert_one(x))
    return results

# именованная функция
def convert3(x):
    return x ** 3

print(transform(data, convert3))
# Лямда = эквивалент предыдущего
print(transform(data, lambda x: x ** 3))
print(transform(data, lambda x: x ** 4))

# Еще один велосипед: фильтрация списка
data = [1, 22, 33, 4, 5, 100]
# results = []
# for x in data:
#     if x > 10:
#         results.append(x)
# print(results)
def select(data, predicate):
    results = []
    for x in data:
        if predicate(x):
            results.append(x)
    return results

print(select(data, lambda x: x > 10))
print(select(data, lambda x: x < 10))

data1 = [(1, 2), (3, 33), (2, 2), (4, 44)]
#Вывести список кортежей (полученных из data1),  у которых второй элемент больше 10
print(select(data1, lambda x: x[1] > 10))

# Стандартные функции Питона для трансформации, фильтрация, сортировки
data = [1, 22, 33, 4, 5, 100]
data1 = [(1, 2), (3, 33), (2, 2), (4, 5)]

# 1.  Трансформация
results = list(map(lambda x: x * x, data))
print(results)

# 2. Фильтрация
results = list(filter(lambda x: x > 10, data))
print(results)

# 3. Сортировка
# results = sorted(data)
results = sorted(data1, key = lambda x: x[1])
print(results)

data1.sort(key = lambda x: x[1])
print(data1)

people = [
    {
        "firstName": "Yuri",
        "lastName": "Andrienko",
        "salary": 123456
    },
    {
        "firstName": "Vasya",
        "lastName": "Pupkin",
        "salary": 77777,
        "children": [
            {
                "firstName": "Petya",
                "gender": "m"
            }
        ]
    },
    {
        "firstName": "Masha",
        "lastName": "Mashkina",
        "salary": 300000
    },
]

# 1. Сортировать людей по возрастанию зарплаты
# 2. Одной строкой кода вывести фамилию самого высокооклачиваемого сотрудника
print(sorted(people, key = lambda p: p['salary']))
print(sorted(people, key = lambda p: -p['salary'])[0]['lastName'])

print(max(people, key = lambda p: p['salary'])['lastName'])