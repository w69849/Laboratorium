import random

def get_fuel_consumption(distance, consumption):
    return consumption/100 * distance

def get_cost(distance, consumed_fuel):
    fuel_prize = 6.5
    return fuel_prize * consumed_fuel


distance = float(input("Podaj droge: "))
consumption = float(input("Podaj spalanie/100km: "))

consumed_fuel = get_fuel_consumption(distance, consumption)

print("Zużycie paliwa: ", consumed_fuel)
print("Koszt podróży: ", get_cost(distance, consumed_fuel))
