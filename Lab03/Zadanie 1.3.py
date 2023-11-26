string = "Python jest super"

print(string[0], string[len(string) - 1])

for i in range(0, len(string), 2):
    print(string[i])

for i in range(1, len(string), 3):
    print(string[i])

for i in range(10, len(string)):
    print(string[i])

print(string[::-1])