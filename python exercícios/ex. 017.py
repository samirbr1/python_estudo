import math

co = float(input("Insert the opposite cathetus: "))
ca = float(input("Insert the adjascent cathetus: "))
# hipotenuse = ((co**2) + (ca**2))**1/2
hipotenuse = math.hypot(co, ca)

print(f"The hipotenuse is {hipotenuse:.2f}")