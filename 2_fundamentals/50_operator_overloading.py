# Operator Overloading - define how operators work on your classes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):          # >
        return True if self.age > other.age else False

    def __add__(self, other):         # +
        return self.age + other.age

    def __str__(self):                # print()
        return f"{self.name} ({self.age})"

roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd)    # True
print(roger + syd)    # 15
print(roger)

# Others: __sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==),
# __lt__ (<), __le__ (<=), __ge__ (>=), __ne__ (!=), __len__ (len())
