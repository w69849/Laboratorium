def sort(list1):
    for e in list1:
        i = 0

        for el in list1:
            if(list1[i] > list1[i+1]):
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp

            i += 1
            if (i >= 2):
                break

    return list1


x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
z = float(input("Podaj z: "))

print(sort([x, y, z]))