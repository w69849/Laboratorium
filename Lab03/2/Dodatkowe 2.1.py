numbers = (input("Podaj 5 cyfr rodzielonych przecinkiem: "))
temp = numbers.split(",")
numbers_list = [int(element) for element in temp]

if(len(numbers_list) != 5):
    exit()

print(numbers_list)

numbers_set = set(numbers_list)

x = numbers_set.pop()

print(f"Wylosowany element: {x}")

if(all(element < x for element in numbers_set)):
    print(f"{x} jest największym elementem tego zbioru")
elif(all(element > x for element in numbers_set)):
    print(f"{x} jest najmniejszym elementem tego zbioru")