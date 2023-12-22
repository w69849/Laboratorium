sentence = str(input("Podaj zdanie: "))
words = sentence.split()
longest = words[0]
longests = [longest]

for i in words:
    if(len(longest) < len(i)):
        longest = i
        longests.clear()
    elif((len(longest) == len(i)) and (longest != i)):
        longests.append(i)

if(len(longests) > 1):
    print(f"Najdłuższe słowa: {longests}")
    print(f"Długość tych słów: {len(longests[0])}")
else:
    print(f"Najdłuższe słowo: {longest}")
    print(f"Jego długość: {len(longest)}")