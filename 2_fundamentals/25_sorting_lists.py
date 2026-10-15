# Sorting Lists
items = ["Roger", "bob", "Syd", "alice"]

# sort() changes the list in place
items.sort()
print(items)             # uppercase comes first

items.sort(key=str.lower)  # case-insensitive
print(items)

# sorted() returns a new list and keeps the original
nums = [5, 2, 9, 1]
new_nums = sorted(nums)
print(nums, new_nums)

print(sorted(nums, reverse=True))

# Copy a list
items_copy = items[:]
print(items_copy)
