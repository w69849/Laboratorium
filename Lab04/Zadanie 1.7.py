def reverse(string):
    reversed_string = ""

    for i in reversed(range(0, len(string))):
        reversed_string += string[i]
    return reversed_string

string = input("Podaj ciąg znaków: ")
print(reverse(string))