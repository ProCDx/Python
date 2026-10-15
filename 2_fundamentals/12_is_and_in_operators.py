# is & in Operators

# 'is' checks if two names point to the SAME object (identity)
a = [1, 2]
b = a
c = [1, 2]
print(a is b)   # True
print(a is c)   # False - equal values, different objects
print(a == c)   # True

# 'in' checks membership in a list, string, dict, set...
print(2 in [1, 2, 3])        # True
print("og" in "Roger dog")   # True
print("name" in {"name": "Roger"})  # True (checks keys)
