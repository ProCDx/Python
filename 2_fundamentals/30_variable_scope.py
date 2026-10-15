# Variable Scope
age = 8   # global variable - visible everywhere

def test():
    print(age)       # can read the global

test()

def local_test():
    color = "brown"  # local - only exists inside this function
    print(color)

local_test()
# print(color)  -> NameError

# To change a global inside a function use the 'global' keyword
count = 0
def increment():
    global count
    count += 1

increment()
print(count)
