# people = [
#     ["Yuri", "Andrienko", 123456],
#     ["Vasya", "Pupkin", 77777],
#     ["Masha", "Mashkina", 300000]
# ]
# for p in people:
#     # print(p)
#     print(f"{p[0]} {p[1]} has salary {p[2]}")
#
# person1 = {
#     "firstName": "Yuri",
#     "lastName": "Andrienko",
#     "salary": 123456
# }
#
# print(f"{person1['firstName']} {person1['lastName']} has salary {person1['salary']}")

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

for p in people:
    print(f"{p['firstName']} {p['lastName']} has salary {p['salary']}")
    if "children" in p.keys():
        print("\tДети:")
        for c in p["children"]:
            print(f"\t\t{c['firstName']}")

# 1. Найти среднюю зарплату
summa= 0
for p in people:
    summa += p['salary']
print(f"Average salary: {summa / len(people)}")
# 2. Вывести фамилию человека с максимальной зарплатой (9:50)
richest = people[0]
for p in people:
    if p['salary'] > richest['salary']:
        richest = p
print(f"Most highly paid is {richest['lastName']}")

nums = (1, 2, 3, 22)
# nums.append(33)
# nums[0] = 111
print(nums)

set1 = {1, 2, 3}
set2 = {2, 3, 3, 4}
set3 = set(nums)
print(set1, set2, set3)
print(set1.union(set2))
print(set.intersection(set2))

person1 = people[0]

for key in person1:
    print(f"{key}: {person1[key]}")

for key, value in person1.items():
    print(f"{key}: {value}")

i = 0
while i < len(people):
    print(f"{people[i]['lastName']}")
    i += 1

iter = iter(people)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))