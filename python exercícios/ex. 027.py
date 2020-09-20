name = str(input("insert your full name: ")).strip().title()
divided_name = name.split()

print(f"Nice to meet you! {divided_name[0]}")
print(f"Your last name is {divided_name[len(divided_name)-1]}")
