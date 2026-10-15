# Objects - everything in Python is an object with attributes and methods
age = 8
print(age.real, age.imag)          # attributes
print(age.bit_length())            # method

items = [1, 2]
items.append(3)                    # method
items.pop()
print(items)

# id() gives the object's identity (memory location)
print(id(age))

# Mutable vs immutable
items_id = id(items)
items.append(4)                    # list is mutable: same object
print(id(items) == items_id)       # True

age_id = id(age)
age += 1                           # int is immutable: a NEW object
print(id(age) == age_id)           # False
