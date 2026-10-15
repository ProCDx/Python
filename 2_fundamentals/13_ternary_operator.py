# Ternary Operator - an if/else in one line

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

def is_adult_ternary(age):
    return True if age > 18 else False

print(is_adult(20), is_adult_ternary(10))

status = "adult" if 25 > 18 else "minor"
print(status)
