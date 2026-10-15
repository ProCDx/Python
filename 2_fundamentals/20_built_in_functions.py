# Built-in Functions (for numbers)
print(abs(-5.5))          # 5.5
print(round(5.49))        # 5
print(round(5.5))         # 6  (banker's rounding: round(4.5) -> 4)
print(round(5.4567, 2))   # 5.46
print(max(3, 7, 1), min(3, 7, 1))
print(sum([1, 2, 3]))
print(pow(2, 3))
print(divmod(7, 2))       # (3, 1)

# The math module has many more
import math
print(math.sqrt(16), math.pi, math.floor(2.7), math.ceil(2.1))
