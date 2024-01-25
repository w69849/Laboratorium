import math

math_functions = []

for i in dir(math):
    if(callable(getattr(math, i))):
        math_functions.append(i)

print("Math: ", math_functions)

tuple_functions = []

for i in dir(tuple):
    if(callable(getattr(tuple, i))):
        tuple_functions.append(i)

print("Tuple: ", tuple_functions)

keyword_functions = []

for i in dir(tuple):
    if(callable(getattr(tuple, i))):
        keyword_functions.append(i)

print("Keyword: ", keyword_functions)