def plus(x: float, y: float, tax: float = 0) -> float:
    result = (x + y) * (1 - tax)
    return result


def minus(x: float, y: float) -> float:
    result = x - y
    return result


def plus_minus(x: float, y: float) -> (float, float):
    result1 = x + y
    result2 = x - y
    return result1, result2


def get_people_from_file(path: str, encoding: str = "utf-8") -> list[dict[str, any]]:
    with open(path, encoding=encoding) as f:
        text = f.read()

    # print(text)
    lines = text.split("\n")
    # print(lines)
    people = []
    for line in lines:
        splitted = line.split(";")
        # print(splitted)
        people.append(
            {
                'firstName': splitted[0],
                'lastName': splitted[1],
                'salary': float(splitted[2])
            }
        )
    return people


if __name__ == "__main__":

    print(plus(1, 2))
    result = plus(2, 3)
    # print(plus("a","b"))

    print(minus(x=1, y=11))
    print(minus(y=100, x=1))

    print(plus(1, 2, tax=0.2))

    a, b = plus_minus(5, 4)
    print(a, b)


    # print(0.8 * 3.0)

    def sum(x, y, *data):
        result = x + y
        for d in data:
            result += d
        return result


    print(sum(1, 2, 44, 55, 66))


    def dummy(x, y, *data1, **data2):
        for key, value in data2.items():
            print(key, value)


    dummy(1, 2, arg1=123, arg2=777, arg3=1024)

    people = get_people_from_file("data/people.csv")
    print(people)
