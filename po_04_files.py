with open("data/people.csv", encoding="utf-8") as f:
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
            'salary':  float(splitted[2])
        }
    )

print(people)