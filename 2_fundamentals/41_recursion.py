# Recursion - a function that calls itself

def factorial(n):
    if n == 1:            # base case - stops the recursion
        return 1
    return n * factorial(n - 1)

print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
