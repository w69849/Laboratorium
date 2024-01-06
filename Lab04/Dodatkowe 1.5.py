def func(a, b):
    c = []
    for i in a:
        for j in b:
            if(i==j):
                if((i in c) == 0):
                    c.append(i)
    return c

print(func([2, 3, 4, 5, 2], [0, 1, 2, 3, 4, 5, 2]))