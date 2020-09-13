from random import choice

i = 0
students = []

while i<4:
    name = input("insert a name:")
    students += [name, ]
    i += 1

print(random.choice(students))
