def get_trapeze_area(a, b, h):
    a = float(a)
    b = float(b)
    h = float(h)

    if (a <= 0 or b <= 0 or h <= 0):
        raise Exception("Musisz podać liczby dodatnie")

    return ((a+b) * h)/2

a = input("Podaj bok a trapezu: ")
b = input("Podaj bok b trapezu: ")
h = input("Podaj wysokość trapezu: ")

try:
    area = get_trapeze_area(a, b, h)
    print("Pole trapezu: ", area)
except ValueError:
    print("Musisz podać liczby dodatnie")
except Exception as e:
    print(e)