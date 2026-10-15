# Functions
def hello():
    print("Hello!")

hello()

# Parameters and arguments
def greet(name):
    print("Hello " + name + "!")

greet("Roger")

# Default parameter values
def greet_default(name="my friend"):
    print("Hello " + name + "!")

greet_default()

# Multiple parameters
def greet_age(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!")

greet_age("Roger", 8)

# Mutable objects are passed by reference
def change(value):
    value["name"] = "Syd"

val = {"name": "Roger"}
change(val)
print(val)   # {'name': 'Syd'}

# Returning values (multiple values come back as a tuple)
def info(name):
    if not name:
        return
    return name, "Roger", 8

print(info("Beau"))
