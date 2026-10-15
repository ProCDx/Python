# Exceptions - handle errors with try / except / else / finally

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    result = 1
else:
    print("No exceptions were raised")
finally:
    print("This always runs")

print(result)

# Raise your own exception
try:
    raise Exception("An error!")
except Exception as error:
    print(error)

# Custom exception class
class DogNotFoundException(Exception):
    print("inside")       # runs when the class is defined
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")
