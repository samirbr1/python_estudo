from random import shuffle


st1 = str(input("first student: "))
st2 = str(input("second student: "))
st3 = str(input("third student: "))
st4 = str(input("fourth student: "))


list_students = [st1, st2, st3, st4]

random.shuffle(list_students)
print(list_students)
