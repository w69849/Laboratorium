sentence = str(input("Podaj zdanie: "))
words = sentence.split()
modified_sentence = ""

for i in range(0, len(words)):
    if(i > 0):
        modified_sentence += ' '

    if(len(words[i]) <= 1):
        modified_sentence += words[i][0].upper()
        continue

    modified_sentence += words[i][0].upper() + words[i][1:-1].lower() + words[i][-1].upper()

print(modified_sentence)