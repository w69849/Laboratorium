name = str(input("Podaj imię: "))
print(f"Witaj {name}")

age = str(input("Podaj wiek: "))
print(f"Twój wiek to: {age}")

full_name = str(input("Podaj imię i nazwisko: "))
print(full_name[0])

for i in range(0, len(full_name)):
    if(full_name[i - 1] == ' '):
        print(full_name[i])

text = str(input("Podaj tekst do wyświetlenia 5 razy: "))

for i in range(0, 5):
    print(text)

string1 = str(input("Podaj 1 łańcuch: "))
string2 = str(input("Podaj 2 łańcuch: "))
string3 = string1 + string2
print(string3)

string4 = str(input("Podaj 1 łańcuch"))
string5 = str(input("Podaj 2 łańcuch"))
string6 = ""

for i in range(0, int(len(string4)/2)):
    string6 += string4[i]

for i in range(int(len(string5)/2), len(string5)):
    string6 += string5[i]

print(string6)

