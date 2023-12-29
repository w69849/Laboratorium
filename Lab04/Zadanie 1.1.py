def get_circle_area(r):
    if(r>0):
        return r*r*3.14

try:
    r = float(input("Podaj pole koła: "))

    if(r <= 0):
        raise ValueError
except ValueError:
    print("Nie ma koła o takim promieniu")
    exit()

print(get_circle_area(r))