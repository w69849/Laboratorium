def get_alphabet():
    temp = []

    for i in range(97, 123):
        temp.append(chr(i))

    return temp

def slice_list(list1, div):
    temp = []
    end = 0
    i = 0

    while(end != 1):
        if(len(list1[i*div:-1]) < div):
            temp.append(list1[i*div:])
            end = 1
        else:
            temp.append(list1[i * div : (i+1) * div])

        i += 1

    return temp

list1 = get_alphabet()
print(list1)

n = int(input("Co ile elementów podzielić listę: "))

list1 = slice_list(list1, n)
print(list1)


