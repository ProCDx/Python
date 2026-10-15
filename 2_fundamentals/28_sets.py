# Sets - unordered collections of unique items
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

print(set1 & set2)   # intersection {'Roger'}
print(set1 | set2)   # union
print(set1 - set2)   # difference {'Syd'}
print(set1 > set2)   # True - set1 is a superset of set2

print(len(set1))
print(list(set1))
print("Roger" in set1)

set1.add("Tina")
set1.remove("Syd")
print(set1)

# Remove duplicates from a list
print(set([1, 1, 2, 3, 3]))
