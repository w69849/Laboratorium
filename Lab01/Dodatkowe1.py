def a(x):
    if(x > 0):
        return 2 * x
    elif(x == 0):
        return 0
    else:
        return -3 * x


def b(x):
    if(x >= 1):
        return x ** 2
    else:
        return x


def c(x):
    if(x > 2):
        return x + 2
    elif(x == 2):
        return 8
    else:
        return x - 4


x = float(input("Podaj x: "))

print(f"a(x) = {a(x)}")
print(f"b(x) = {b(x)}")
print(f"c(x) = {c(x)}")