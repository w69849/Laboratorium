def is_positive(x):
    if(x > 0):
        print("Ta liczba jest dodatnia")
    else:
        print("Ta liczba nie jest dodatnia")

try:
    x = float(input("Podaj liczbę: "))
except ValueError:
    print("To nie jest liczba")
    exit()

is_positive(x)