# Lambda Functions - small anonymous one-expression functions
# lambda arguments: expression

double = lambda num: num * 2
print(double(2))         # 4

multiply = lambda a, b: a * b
print(multiply(2, 4))    # 8

# Handy as a sort key
dogs = [("Roger", 8), ("Syd", 3), ("Tina", 5)]
print(sorted(dogs, key=lambda d: d[1]))
