phrase = str(input("Write a phrase here: ")).strip().upper()

counter = phrase.count("A")
first = phrase.find("A")
last = phrase.rfind("A")

print(f"The letter A appeared {counter} times in the phrase")
print(f"The first position wich the letter A appeared is {first + 1} ")
print(f"The last position wich the letter A appeared is {last + 1} ")

