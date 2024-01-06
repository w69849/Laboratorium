def is_palindrome(string):
    if(string == string[::-1]):
        print("To jest palindrom")
        return 1
    else:
        print("To nie jest palindrom")
        return 0

string = input("Podaj napis: ")

is_palindrome(string)