def calculate(choice, a, b):
    return {
        '1': a + b,
        '2': a - b,
        '3': a * b,
        '4': a / b,
        '5': a ** b
    }.get(choice, "Zły wybór!")


print("Jaką operację chcesz wykonać?\n"
      "1) dodawanie \n"
      "2) odejmowanie \n"
      "3) mnożenie \n"
      "4) dzielenie \n"
      "5) potęgowanie")

choice = (input("Wpisz numer operacji: "))
if(not choice.isdigit()):
    print("Zły wybór!")
elif(int(choice) < 1 or int(choice) > 5):
    print("Zły wybór!")
else:
    number1 = float(input("Podaj argument 1: "))
    number2 = float(input("Podaj argument 2: "))

    result = calculate(choice, number1, number2)
    print(f"Wynik: {result}")