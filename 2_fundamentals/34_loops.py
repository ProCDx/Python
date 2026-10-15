# Loops

# while loop - repeats while the condition is True
count = 0
while count < 3:
    print("The condition is True", count)
    count += 1
print("After the loop")

# for loop - iterate over items
items = [1, 2, 3, 4]
for item in items:
    print(item)

# range()
for item in range(4):     # 0, 1, 2, 3
    print(item)

# enumerate() gives index and value
for index, item in enumerate(["a", "b", "c"]):
    print(index, item)
