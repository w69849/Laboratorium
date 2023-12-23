lista_zakupow = \
    {
        "obudowa" : 400,
        "GPU" : 1500,
        "CPU" : 600,
        "płyta_główna" : 800,
        "dysk" : 300,
        "RAM" : 300,
        "zasilacz" : 300,
        "chłodzenie" : 300
    }

print(lista_zakupow)
print("Łączna cena: ", sum(lista_zakupow.values()))