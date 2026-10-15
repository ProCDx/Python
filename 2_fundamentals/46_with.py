# With - the 'with' statement handles setup/cleanup (e.g. closing files)

# Without with:
file = open("example.txt", "w")
try:
    file.write("Hello from Python!\n")
finally:
    file.close()

# With with - the file closes automatically:
with open("example.txt", "a") as file:
    file.write("Added with 'with'\n")

with open("example.txt") as file:
    print(file.read())
