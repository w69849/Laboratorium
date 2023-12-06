n = int(input("Podaj liczbe studentów: "))

i = 1
points = 0

while(n >= i):
    x = int(input(f"Podaj liczbe punktów studenta {i}: "))
    points += x
    i += 1

print(f"Średnia liczba punktów w grupie: {points/n}")