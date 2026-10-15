# Booleans
done = False
done = True

if done:
    print("yes")
else:
    print("no")

# Truthiness: these are False -> 0, 0.0, "", [], {}, (), set(), None
print(bool(0), bool(""), bool([]), bool(None))
# Everything else is True
print(bool(1), bool("hi"), bool([0]))

# any() -> True if at least one is True. all() -> True only if all are True
book_1_read = True
book_2_read = False
print(any([book_1_read, book_2_read]))   # True
print(all([book_1_read, book_2_read]))   # False
