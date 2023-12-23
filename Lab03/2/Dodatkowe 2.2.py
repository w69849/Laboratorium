enemies = ((0,1), (2,3), (2,4), (3,4))
coins = ((1,1),(2,0),(3,3),(5,3))

for i in range(0, 5):
    for j in range(0, 6):
        if(i == 2):
            print('=', end='')
        elif((j, i) in enemies):
            print('x', end='')
        elif((j, i) in coins):
            print('*', end='')
        else:
            print('.', end='')

    print("")
