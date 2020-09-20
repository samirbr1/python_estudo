num = int(input("Insert a number:"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analysing the number {num}")
print(f"unity: {u}")
print(f"dez: {d}")
print(f"cen: {c}")
print(f"mil: {m}")
#n = str(num)

#print(f"unidade {n[3]}")
#print(f"dezena {n[2]}")
#print(f"centena {n[1]}")
#print(f"milhar {n[0]}")
