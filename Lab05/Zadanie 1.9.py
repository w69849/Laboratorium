import random

try:
    min = int(input("Podaj dolny zakres losowania: "))
    max = int(input("Podaj górny zakres losowania: "))

    number = random.randint(min, max)

    life = 3

    while(life):
        x = input("Strzelaj: ")

        if(not x.isdigit()):
            print("Musisz podać liczbę całkowitą")
            continue
        else:
            x = int(x)

            if(x == number):
                print("Udało ci się zgadnąć!")
                exit()
            else:
                if(x<number):
                    print("To za mało")
                else:
                    print("To za dużo")

                if(life==1):
                    print("Skończyły ci się szanse")
                life -= 1
except ValueError:
    print("Musisz podać liczbę całkowitą")
    exit()