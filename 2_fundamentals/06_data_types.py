# Data Types
name = "Roger"          # str
age = 8                 # int
height = 1.75           # float
is_dog = True           # bool
numbers = [1, 2, 3]     # list
point = (1, 2)          # tuple
dog = {"name": "Roger"} # dict
unique = {1, 2, 3}      # set
nothing = None          # NoneType
z = 2 + 3j              # complex
r = range(5)            # range

for value in [name, age, height, is_dog, numbers, point, dog, unique, nothing, z, r]:
    print(repr(value), "->", type(value))

# Check a type
print(type(name) == str)
print(isinstance(age, int))

# Convert (cast) between types
print(int("20") + 1)
print(float(age))
print(str(age) + " years")
