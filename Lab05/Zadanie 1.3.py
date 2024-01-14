import time

t = int(input("Podaj czas w sekundach: "))

while(t):
    print(t)
    time.sleep(1)
    t -= 1