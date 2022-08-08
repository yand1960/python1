import datetime as dt


def days_till_new_year():
    today = dt.date.today()
    new_year = dt.date(today.year + 1, 1, 1)
    return (new_year - today).days


if __name__ == "__main__":
    days_left = days_till_new_year()
    print(days_left)

    x = 2
    y = 2
    z = 2 + 2
    print(f"{x}+{y}={z}")

    first_name = "Yuri"
    last_name = "Andrienko"
    full_name = first_name + " " + last_name
    print(full_name)
    name_with_initial = f"{first_name[0:2]}.{last_name}"
    print(name_with_initial)

    full_name = "Vasya Pupkin"
    space_positon = full_name.find(" ")
    first_name = full_name[0:space_positon]
    last_name = full_name[space_positon + 1:]
    print(last_name, first_name)

    numbers = [1, 2, 3, 44, 4, 55, 5]
    numbers.append(666)
    for x in numbers:
        if x > 4:
            print(x)

    # for i in range(1, 4):
    #     print(numbers[i])

    people = ["Yuri", "Vasya","Masha"]
    for p in people:
        print(p)

    print(people)

    for p in people:
        print(p, end=" ")

    output = ""
    for p in people:
        output += p + ","
    # output = output[0: len(output) - 1]
    output = output[0:-1]
    print(output)

    data1 = [1, 2, 3]
    data2 = [3, 2, 0]

    for x1 in data1:
        for x2 in data2:
            if x1 == x2:
                print(x1)

    results = set(data1).intersection(set(data2))
    print(results)

