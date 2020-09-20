name = str(input("Insert your name: ")).strip()

print(f"Your name in uppercase is {name.upper()}")
print(f"Your name in lowercase is {name.lower()}")
print(f"The lenght of your name is {len(name)-name.count(' ')}")
divide = name.split()
print(f"Your first name is {(divide[0])} and has {len(divide[0])} letters")