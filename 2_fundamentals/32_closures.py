# Closures - an inner function remembers variables from its outer scope
# even after the outer function has finished.

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment

increment = counter()
print(increment())   # 1
print(increment())   # 2
print(increment())   # 3
