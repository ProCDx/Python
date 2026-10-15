# Bitwise Operators (rarely used, but good to know)
a = 0b1100   # 12
b = 0b1010   # 10

print(a & b, bin(a & b))    # AND
print(a | b, bin(a | b))    # OR
print(a ^ b, bin(a ^ b))    # XOR
print(~a)                   # NOT
print(a << 1)               # left shift  (24)
print(a >> 1)               # right shift (6)
