# Lists
dogs = ["Roger", "Syd", 1, True]   # can mix types

print("Roger" in dogs)   # True
print(dogs[0], dogs[-1])

dogs[2] = "Beau"         # change an item
print(dogs)

print(dogs.index("Syd"))
print(dogs[1:3])         # slicing
print(len(dogs))

# Adding items
dogs.append("Judah")
dogs.extend(["Quincy", 5])
dogs += ["Bella"]
dogs.insert(1, "Max")
dogs[1:1] = ["Test1", "Test2"]   # insert several at index 1
print(dogs)

# Removing items
dogs.remove("Quincy")
last = dogs.pop()        # removes and returns the last item
print(last, dogs)

empty = []
print(empty)
