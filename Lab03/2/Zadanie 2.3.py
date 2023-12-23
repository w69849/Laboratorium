rachunki = \
    {
        "styczeń" : 300,
        "luty" : 280,
        "marzec" : 310,
        "kwiecień" : 270,
        "maj" : 260,
        "czerwiec" : 230,
        "lipiec" : 250,
        "sierpień" : 220,
        "wrzesień" : 260,
        "październik" : 290,
        "listopad" : 320
    }

average = sum(rachunki.values()) / len(rachunki)

print(" Cena maksymalna: ", max(rachunki.values()), '\n',
      "Cena minimalna: ", min(rachunki.values()), '\n',
      "Cena średnia: ", average)

if(float(list(rachunki.values())[-1]) > average):
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")