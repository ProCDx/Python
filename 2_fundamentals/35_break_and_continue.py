# Break and Continue
items = [1, 2, 3, 4]

# continue skips to the next iteration
for item in items:
    if item == 2:
        continue
    print(item)        # 1 3 4

print("---")

# break exits the loop entirely
for item in items:
    if item == 2:
        break
    print(item)        # 1
