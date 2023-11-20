age = int(input("Wprowadź wiek klienta: "))
prize = 10

if(age < 4):
    print("Cena biletu: 0")
elif(age >= 4 and age <= 18):
    print(f"Cena biletu: {prize}")
else:
    print(f"Cena biletu: {prize * 2}")