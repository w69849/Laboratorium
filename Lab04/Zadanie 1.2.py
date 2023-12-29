def get_trapeze_area(a, b, h):
    return ((a+b) * h)/2

try:
    a = float(input("Podaj bok a trapezu: "))
    b = float(input("Podaj bok b trapezu: "))
    h = float(input("Podaj wysokość trapezu: "))

    if(a<=0 or b<=0 or h<=0):
        raise Exception("Złe wymiary trapezu")
except ValueError:
    print("Niepoprawna wartość")
    exit()
except Exception as e:
    print(e)
    exit()

print("Pole trapezu: ", get_trapeze_area(a, b, h))