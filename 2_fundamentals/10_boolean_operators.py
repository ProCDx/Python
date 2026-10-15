# Boolean Operators: not, and, or
condition1 = True
condition2 = False

print(not condition1)               # False
print(condition1 and condition2)    # False
print(condition1 or condition2)     # True

# 'or' returns the first truthy operand (or the last one)
print(0 or 1)               # 1
print(False or "hey")       # hey
print("hi" or "hey")        # hi

# 'and' returns the first falsy operand (or the last one)
print(0 and 1)              # 0
print(1 and 0)              # 0
print("hi" and "hey")       # hey
