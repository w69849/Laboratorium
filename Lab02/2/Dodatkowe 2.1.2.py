import math

while(0 == 0):
    dana = input("Podaj zmienną: ")

    if(dana.isdigit() and int(dana) >= 0):
        print(math.sqrt(int(dana)))
    else:
        print("dziękujemy za skorzystanie z naszej aplikacji")
        break