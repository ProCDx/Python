# Map, Filter, Reduce
numbers = [1, 2, 3]

# map() applies a function to every item
result = map(lambda a: a * 2, numbers)
print(list(result))      # [2, 4, 6]

# filter() keeps items where the function returns True
result = filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(result))      # [2, 4, 6]

# reduce() combines items into a single value
from functools import reduce

expenses = [("Dinner", 80), ("Car repair", 120)]
total = reduce(lambda a, b: a[1] + b[1], expenses)
print(total)             # 200

# Same thing, more readable:
print(sum(map(lambda e: e[1], expenses)))
