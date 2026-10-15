# Classes - blueprints for creating objects

class Animal:
    def walk(self):
        print("Walking..")

class Dog(Animal):               # Dog inherits from Animal
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)
print(type(roger))
print(roger.name, roger.age)
roger.bark()
roger.walk()                     # inherited method
