sentence = str(input("Podaj zdanie: "))
sentence2 = ""

for i in range (0, len(sentence)):
    if((i == 0) or (i%2 == 0)):
        sentence2 += sentence[i]

print(sentence2)