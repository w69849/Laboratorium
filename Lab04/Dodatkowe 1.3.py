import math

def quadratic_equation(a, b=0, c=0):
    a = float(a)
    b = float(b)
    c = float(c)

    if(a == 0):
        raise Exception("Współczynnik a nie może być równy 0")

    delta = (b*b) - (4*a*c)

    if(delta < 0):
        print("To równanie nie ma rozwiązań")
    elif(delta == 0):
        x0 = (-b)/(2*a)

        print(x0)

        return x0
    else:
        x1 = ((-b) - (math.sqrt(delta))) / (2*a)
        x2 = ((-b) + (math.sqrt(delta))) / (2*a)

        print(f"x1 = {x1}", f"x2 = {x2}")

        return x1, x2


while(0 == 0):
    a = input("Podaj współczynnik a: ")
    b = input("Podaj współczynnik b: ")
    c = input("Podaj współczynnik c: ")

    try:
        quadratic_equation(a, b, c)
        exit()
    except ValueError:
        print("Musisz podać liczby")
    except Exception as e:
        print(e)