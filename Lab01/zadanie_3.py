def get_area(a, b):
    return a * b

def get_circumference(a, b):
    return 2*a + 2*b


a = int(input("Podaj bok a: "))
b = int(input("Podaj bok b: "))

print("Pole: ", get_area(a, b))
print("Obwód: ", get_circumference(a, b))
