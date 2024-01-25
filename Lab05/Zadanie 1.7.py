import random

min = int(input("Podaj dolny zakres przedziału: "))
max = int(input("Podaj górny zakres przedziału: "))

numbers = []

for i in range(0, 10):
    numbers.append(random.randint(min, max))

tuple1 = tuple(numbers)
print(tuple1)

x = 1

for i in tuple1:
    x *= i

print("Średnia geometryczna krotki: ", x ** (1/len(tuple1)))