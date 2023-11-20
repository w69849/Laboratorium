letter = input("Wprowadź literę: ")

if(letter.isupper()):
    print("Duża litera")
elif(letter.islower()):
    print("Mała litera")
else:
    print("To nie jest litera")