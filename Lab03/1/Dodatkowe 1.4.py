string = str(input("Podaj ciąg znaków: "))
set1 = set()
modified_string = ""

for i in string:
    if(i in set1):
        modified_string += '@'
    else:
        set1.add(i)
        modified_string += i

print(modified_string)