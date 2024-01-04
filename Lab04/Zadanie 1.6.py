import math

def get_triangle_area(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    if(a<=0 and b<=0 and c<=0):
        raise ValueError

    if(max(a,b,c) == a):
        if(a >= b+c):
            raise Exception("Najdłuższy bok musi być krótszy niż suma dwóch pozostałych boków")
    elif(max(a, b, c) == b):
        if (b >= a+c):
            raise Exception("Najdłuższy bok musi być krótszy niż suma dwóch pozostałych boków")
    elif(max(a, b, c) == c):
        if (c >= b+a):
            raise Exception("Najdłuższy bok musi być krótszy niż suma dwóch pozostałych boków")

    circumference = (a+b+c) / 2

    return math.sqrt(circumference * (circumference - a) * (circumference - b) * (circumference - c))

a = input("Podaj bok a: ")
b = input("Podaj bok b: ")
c = input("Podaj bok c: ")

try:
    print(get_triangle_area(a, b, c))
except ValueError:
    print("Musisz podać liczby dodatnie")
except Exception as e:
    print(e)