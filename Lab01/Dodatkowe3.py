def convert(c):
    if(c.isupper()):
        return c.lower()
    elif(c.islower()):
        return c.upper()
    else:
        return "Wrong input"


c = input("Podaj literę: ")

print(convert(c))