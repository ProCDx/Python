# Strings
name = "Roger"
also_name = 'Roger'      # single or double quotes

# Concatenate
phrase = name + " is a good dog"
name += " the dog"
print(phrase)
print(name)

# Convert to string
age = str(8)
print(age, type(age))

# Multi-line strings
print("""Roger is
    8
years old""")

# f-strings
print(f"{phrase} and he is {age} years old")
