def solve_equation(a, b):
    return (-1*b)/a


a = float(input("Współczynnik a: "))
b = float(input("Współczynnik b: "))

print(f"x = {solve_equation(a, b)}")