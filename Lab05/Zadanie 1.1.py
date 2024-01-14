import random

lucky_number = random.randint(1, 11)
print(f"Szczęśliwy numer: {lucky_number}")

years = [1994, 1998, 2001, 2002, 2003, 2004]
lucky_year = random.choice(years)
print(f"Szczęśliwy rocznik: {lucky_year}")

numbers = []

for i in range(0, 50):
    numbers.append(i)

print(f"Wylosowane liczby: {random.sample(numbers, 6)}")