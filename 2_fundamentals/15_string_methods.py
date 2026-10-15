# String Methods
name = "  Roger the Dog  "

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())               # remove whitespace both sides
print(name.lstrip(), name.rstrip())
print(name.replace("Dog", "Puppy"))
print(name.split())               # ['Roger', 'the', 'Dog']
print("-".join(["a", "b", "c"]))  # a-b-c
print(name.find("the"))           # index of substring
print("roger".startswith("ro"), "roger".endswith("er"))
print("abc".isalpha(), "123".isdigit(), "abc1".isalnum())
print("Roger".islower(), "ROGER".isupper())

# Strings are immutable: methods return NEW strings
original = "roger"
upper = original.upper()
print(original, upper)

# Built-in function len()
print(len("Roger"))
