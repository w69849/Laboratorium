import math

def get_area(a, b, c):
    temp1 = (a+b+c) / 2
    temp2 = temp1 * (temp1 - a) * (temp1 - b) * (temp1 - c)
    return math.sqrt(temp2)


a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
c = float(input("Podaj bok c: "))

print(f"Pole trójkąta: {get_area(a, b, c)}")