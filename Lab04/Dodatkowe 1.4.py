def fun(string):
    string = str(string)

    upper_letters = 0
    lower_letters = 0
    others = 0

    for i in string:
        if(i.isupper()):
            upper_letters += 1
        elif(i.islower()):
            lower_letters += 1
        else:
            others += 1

    return \
        {
            "Duże_litery" : upper_letters,
            "Małe litery" : lower_letters,
            "Pozostałe znaki" : others
        }


string = input("Podaj napis: ")

print(fun(string))