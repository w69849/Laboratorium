n = int(input("Podaj liczbę naturalną: "))
factorial = 1

if(n == 0):
    factorial = 0
else:
    for i in range(1, n+1):
        factorial *= i

print(f"Silnia: {factorial}")