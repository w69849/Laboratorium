def get_circle_area(r):
    r = float(r)

    if (r <= 0):
        raise ValueError
    else:
        print("Pole koła: ", r*r*3.14)

r = input("Podaj promień koła: ")

try:
    get_circle_area(r)
except ValueError:
    print("Nie ma koła o takim promieniu")