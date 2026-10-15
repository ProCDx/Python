# List Comprehension (called "List Compression" in the video)
# A compact way to build lists: [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]

# loop version
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n ** 2)

# comprehension version
numbers_power_2 = [n ** 2 for n in numbers]
print(numbers_power_2)

# map version
numbers_power_2 = list(map(lambda n: n ** 2, numbers))
print(numbers_power_2)

# with a condition
evens = [n for n in numbers if n % 2 == 0]
print(evens)
