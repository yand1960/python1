# Пример класса данных
class Person:

    def __init__(self, first_name: str, last_name: str, salary: float):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        # return f"Person: {self.first_name} {p.last_name}"
        return self.__dict__.__str__()


if __name__ ==  "__main__":

    people: [Person] = []
    people.append(Person(first_name="Yuri", last_name="Andrienko", salary=123456))
    people.append(Person(first_name="Vasya", last_name="Pupkin", salary=77777))
    people.append(Person(first_name="Masha", last_name="Mashkina", salary=30000))

    for p in people:
        # print(f"{p.first_name} {p.last_name} has salary {p.salary}")
        print(p)

    print(max(people, key=lambda p: p.salary ).last_name)