g = int(input("Podaj wysokość choinki: "))
c = ' '

for i in range(1, g + 1):
    print((c * (g-i)), end = '')

    for j in range(i):
        print('* ', end = '')
    print('')