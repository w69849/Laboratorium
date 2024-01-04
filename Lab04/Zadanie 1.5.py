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

height = int(input("Podaj wzrost (w centymetrach): "))
weight = int(input("Podaj wagę (w kg): "))

bmi, bmi_range = get_bmi(weight, height)
print(bmi_range)