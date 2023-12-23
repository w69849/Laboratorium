import random

def create_list(n, x):
    list2 = []

    for i in range(0, n):
        s = ""

        for j in range(0, random.randint(1, x)):
            s += chr(random.randint(97, 122))

        list2.append(s)

    return list2

n = int(input("Podaj liczbę elementów listy: "))
x = int(input("Podaj maksymalną liczbę znaków elementu: "))
list1 = create_list(n, x)

print(list1)

##########################################  a
count = 0

for i in range(0, len(list1)):
    count += len(list1[i])

print(f"Liczba znaków w liście: {count}")

#########################################   b
count = 0

for i in range(0, len(list1)):
    count += list1[i].count('k')

print(f"Ilość liter k: {count}")

########################################    c
count = 0

for i in range(0, len(list1)):
    count += list1[i].count('kt')

print(f"Ilość ciągów znaków 'kt': {count}")

########################################    d
s = int(input("Podaj długość elementu: "))

count = 0

for i in range(0, len(list1)):
    if(len(list1[i]) > s):
        count += 1

print(f"Ilość elementów dłuższych od {s}: {count}")

########################################    e
for i in range(0, len(list1)):
    list1[i] = 'a' + list1[i] + 'z'

print(list1)
