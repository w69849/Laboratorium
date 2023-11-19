def get_area(a, b):
    return a * b


def get_circumreference(a, b):
    return 2*a + 2*b


a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))

print(get_area(a, b))
print(get_circumreference(a, b))