def fun(name):
    if(name.isalpha() == 0):
        raise ValueError

    gender = ""

    if(name[len(name) - 1] == 'a'):
        gender = "kobieta"
    else:
        gender = "mężczyzna"

    return gender

name = input("Podaj imię: ")

try:
    print(fun(name))
except ValueError:
    print("Imię musi zawierać tylko litery")

names = ["Michał", "Paweł", "Anna", "Stanisław", "Ewa"]
dict1 = dict()

for i in names:
    dict1[i] = fun(i)

print(dict1)

