import random

x = set()
y = set()

a = random.randint(3, 7)
b = random.randint(3, 7)

for i in range(0, a):
    x.add(random.randint(0, 10))

for i in range(0, b):
    y.add(random.randint(0, 10))

print(f" Zbiór X: {x}\n", f"Zbiór Y: {y}\n")

if(5 in x):
    print("Zbiór X zawiera liczbę 5")
else:
    print("Zbiór X nie zawiera liczby 5")

if(x.issubset(y)):
    print("Zbiór X jest podzbiorem Y")
else:
    print("Zbiór X nie jest podzbiorem Y")

if(y.issubset(x)):
    print("Zbiór Y jest podzbiorem X")
else:
    print("Zbiór Y nie jest podzbiorem X")

if(x.issuperset(y)):
    print("Zbiór X jest nadzbiorem Y")
else:
    print("Zbiór X nie jest nadzbiorem Y")

if(y.issuperset(x)):
    print("Zbiór Y jest nadzbiorem X")
else:
    print("Zbiór Y nie jest nadzbiorem X")

print("Suma zbiorów: ", x.union(y))

print("Różnica zbiorów X i Y: ", x.difference(y))

print("Różnica zbiorów Y i X: ", y.difference(x))

print("Iloczyn zbiorów: ", x.intersection(y))

print("Różnica symetryczna zbiorów: ", x.symmetric_difference(y))

print("Największy element zbioru X: ", max(x))
print("Największy element zbioru Y: ", max(y))

y.add(x.pop())

y.update(x)

x.clear()
y.clear()
