# Polymorphism - different classes share a method name,
# so the same code works with any of them.

class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

animal1 = Dog()
animal2 = Cat()

for animal in [animal1, animal2]:
    animal.eat()
