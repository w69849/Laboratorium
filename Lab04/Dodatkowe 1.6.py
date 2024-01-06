def nwd(a, b):
    a = int(a)
    b = int(b)

    while(b):
        a, b = b, a%b

    if(a < 0):
        a *= -1
    return a

a = input("Podaj 1 liczbe: ")
b = input("Podaj 2 liczbe: ")

try:
    print(nwd(a,b))
except ValueError:
    print("Musisz podać liczby całkowite")