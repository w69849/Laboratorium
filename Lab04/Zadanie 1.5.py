def get_bmi(weight, height):
    weight = int(weight)
    height = int(height)

    if (height <= 0):
        raise Exception("Musisz podać liczby dodatnie")

    if (weight <= 0):
        raise Exception("Musisz podać liczby dodatnie")

    bmi = weight / ((height/100) ** 2)
    range = ""

    if(bmi < 18.5):
        range = "Niedowaga"
    elif(18.5 <= bmi < 24.9):
        range = "Prawidłowa waga"
    elif(25 <= bmi < 29.9):
        range = "Nadwaga"
    elif(bmi > 29.9):
        range = "Otyłość"

    return bmi, range

height = input("Podaj wzrost (w centymetrach): ")
weight = input("Podaj wagę (w kg): ")

try:
    bmi, bmi_range = get_bmi(weight, height)
    print(bmi_range)
except ValueError:
    print("Musisz podać liczby całkowite")
except Exception as e:
    print(e)


