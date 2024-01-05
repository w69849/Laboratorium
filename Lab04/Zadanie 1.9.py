def fib(n):
    n = int(n)

    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = input("Podaj numer wyrazu ciągu Fibonacciego: ")

try:
    print(fib(n))
except ValueError:
    print("Musisz podać liczbę całkowitą dodatnią")