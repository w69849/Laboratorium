n = int(input("Podaj liczbę elementów ciągu arytmetycznego do wypisania: "))
a = int(input("Podaj 1 element ciągu: "))
r = int(input("Podaj r: "))

for i in range(n):
    print(a + (i*r))