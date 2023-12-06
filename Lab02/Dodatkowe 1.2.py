n = int(input("Podaj liczbe studentów: "))

i = 1
points = 0

while(0 == 0):
    x = int(input(f"Podaj liczbe punktów studenta {i}: "))
    i += 1

    if(x>100 or x<0):
        continue

    points += x
    break


print(f"Średnia liczba punktów w grupie: {points/n}")