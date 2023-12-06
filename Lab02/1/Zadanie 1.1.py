x = int(input("Podaj liczbe1: "))
y = int(input("Podaj liczbe1: "))

if(x <= y):
    for i in range(x, y + 1):
        if(i%2 != 0):
            continue
        print(i)
else:
    for i in range(y, x + 1):
        if (i % 2 != 0):
            continue
        print(i)