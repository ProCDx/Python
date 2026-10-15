# Tuples - like lists but immutable (cannot be changed)
names = ("Roger", "Syd")

print(names[0], names[-1])
print(names.index("Syd"))
print(len(names))
print("Roger" in names)
print(names[0:1])
print(sorted(names))     # returns a list

# You can create a new tuple from existing ones
new_tuple = names + ("Tina", "Quincy")
print(new_tuple)

# Tuple unpacking
first, second = names
print(first, second)

# names[0] = "X"  -> TypeError: tuples are immutable
