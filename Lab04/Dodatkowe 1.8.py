def is_anagram(string1, string2):
    flag = 0

    if(len(string1) == len(string2)):
        for i in string1:
            for j in string2:
                if(i == j):
                    flag = 1
                    break
                else:
                    flag = 0

    if(flag):
        print("Te wyrazy są anagramami")
        return 1
    else:
        print("Te wyrazy nie są anagramami")
        return 0

string1 = input("Podaj pierwszy wyraz: ")
string2 = input("Podaj drugi wyraz: ")

is_anagram(string1, string2)