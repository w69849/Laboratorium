rain = input("Pada deszcz? (y/n): ")
bus = input("Jest autobus? (y/n): ")

if(rain == 'y'):
    if(bus == 'y'):
        print("Weź parasol. Dostanies się na uczelnię")
    elif(bus == 'n'):
        print("Nie dostaniesz się na uczelnię")
    else:
        print("Niepoprawny znak")
elif(rain == 'n'):
    if(bus == 'y'):
        print("Dostaniesz się na uczelnię. Miłego dnia i pięknej pogody")
    elif(bus == 'n'):
        print("Nie dostaniesz się na uczelnię")
    else:
        print("Niepoprawny znak")
else:
    print("Niepoprawny znak")