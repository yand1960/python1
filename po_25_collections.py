from collections import deque, namedtuple

q1 = deque([1, 2, 3])
q1.append(44)
q1.appendleft(-77)
print(q1)

Person = namedtuple("Person", ["firstname", "lastname"])

p1 = Person(firstname="Yuri", lastname="Andrienko")
print(f"{p1.firstname} {p1.lastname}")
