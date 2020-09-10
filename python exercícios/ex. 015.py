days = int(input("How many days with the car? "))
kilometers = int(input("How many kilometers? "))

price = (60 * days) + (0.15 * kilometers)

print(f"The price to pay for {days} and {kilometers} kilometers is R$ {price}")