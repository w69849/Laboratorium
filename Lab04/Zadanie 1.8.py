import math
import fractions

def power(a, n):
    a = float(a)
    n = float(n)

    if(n < 0):
        a = a * 1/(a*a)
        n *= -1

    if(n%1 != 0):
        if (a < 0):
            raise Exception("Nie liczymy tutaj potęg o ujemnej podstawie i wymiernym wykładniku :(")

        fraction = fractions.Fraction(n).limit_denominator()
        numerator = fraction.numerator
        denominator = fraction.denominator

        return round((a ** (numerator/denominator)), 5)

    if(n == 0):
        return 1
    else:
        return round(a * power(a, n-1), 5)

a = input("Podaj podstawę potęgi: ")
n = input("Podaj wykładnik potęgi: ")

try:
    print(power(a, n))
except ValueError:
    print("Musisz podać liczby")
except Exception as e:
    print(e)