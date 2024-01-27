import math

def get_area(a, b, x):
    a = float(a)
    b = float(b)
    x = float(x)

    if (x < 0 or x >= 90):
        raise Exception("Niepoprawna wartość kąta")

    c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(x)))

    if((c > a+b) or (a > b+c) or (b > a+c)):
        raise Exception("Taki trójkąt nie istnieje")

    return ((a*b*math.sin(math.radians(x))) / (2))

try:
    a = input("Podaj bok a: ")
    b = input("Podaj bok b: ")
    x = input("Podaj kąt między tymi bokami: ")

    print(get_area(a, b, x))
except ValueError:
    print("Musisz podać liczby dodatnie")
    exit()
except Exception as e:
    print(e)
    exit()