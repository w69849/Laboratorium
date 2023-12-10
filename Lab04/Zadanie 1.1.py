def get_circle_area(r):
    if(r>0):
        return r*r*3.14
    else:
        print("Nie można obliczyć pola:")

r = float(input("Podaj pole koła: "))

print(get_circle_area(r))