def get_bmi(weight, height):
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

try:
    height = int(input("Podaj wzrost (w centymetrach): "))

    if(height <= 0):
        raise Exception("Musisz podać liczbę dodatnią")

    weight = int(input("Podaj wagę (w kg): "))

    if(weight <= 0):
        raise Exception("Musisz podać liczbę dodatnią")
except ValueError:
    print("To nie jest liczba całkowita")
    exit()
except Exception as e:
    print(e)
    exit()

bmi, bmi_range = get_bmi(weight, height)
print(bmi_range)