def is_positive(x):
    x = float(x)

    if(x > 0):
        print("Ta liczba jest dodatnia")
    else:
        print("Ta liczba nie jest dodatnia")

x = input("Podaj liczbę: ")

try:
    is_positive(x)
except ValueError:
    print("To nie jest liczba")