sentence = str(input("Podaj zdanie: "))

sentence = sorted(sentence)

for i in sentence:
    if(i != ' '):
        print(i)

alphabet = set('aąbcćdeęfghijklłmnoprstuvwxyz')

for i in range(0, len(sentence)):
    sentence[i] = sentence[i].lower()

missing_letters = alphabet - set(sentence)

print("Brakujące litery: ", sorted(missing_letters))