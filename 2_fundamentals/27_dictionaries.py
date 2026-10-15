# Dictionaries - key: value pairs
dog = {"name": "Roger", "age": 8}

print(dog["name"])
dog["name"] = "Syd"
print(dog.get("name"))
print(dog.get("color", "brown"))   # default if key missing

dog["favorite food"] = "Meat"      # add a key
print(dog)

print(dog.pop("favorite food"))    # remove and return
print(dog.popitem())               # removes the last inserted item
print(dog)

dog = {"name": "Roger", "age": 8}
print("name" in dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))

del dog["age"]
print(dog)

dog_copy = dog.copy()
print(dog_copy)

for key, value in {"a": 1, "b": 2}.items():
    print(key, value)
