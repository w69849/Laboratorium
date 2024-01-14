import datetime

last = datetime.date(2023, 12, 10)
print("Data ostatnich laboratoriów: ", last.strftime("%Y %B %I"))
kolokwium = datetime.date(2024, 2, 11)
print("Data kolokwium: ", kolokwium.strftime("%Y %B %I"))

print("Od ostatnich laboratoriów upłynęło: ", (datetime.date.today() - datetime.date(2023, 12, 10)).days, "dni")
print("Do kolokwium zostało: ", (datetime.date(2024, 2, 11) - datetime.date.today()).days, "dni")