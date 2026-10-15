# String Characters & Slicing
name = "Roger"

print(name[0])     # R  (first char, index starts at 0)
print(name[1])     # o
print(name[-1])    # r  (last char)
print(name[-2])    # e

# Slicing [start:end]  - end is not included
print(name[0:2])   # Ro
print(name[:2])    # Ro
print(name[2:])    # ger
print(name[1:-1])  # oge
print(name[::-1])  # regoR  (reverse with a step of -1)
