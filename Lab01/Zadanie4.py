import math

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = (b**2) - (4*a*c)

if(delta < 0):
    print("To równanie nie ma rozwiązań")
elif(delta == 0):
    x = (-1*b) / (2*a)
    print(f"x = {x}")
else:
    x1 = ((-1*b) - math.sqrt(delta)) / (2*a)
    x2 = ((-1*b) + math.sqrt(delta)) / (2*a)
    print(f"x1 = {x1}\n"
          f"x2 = {x2}")