# Escaping Characters - use a backslash \

print("Ro\"ger")         # double quote inside double quotes
print('Ro\'ger')         # single quote inside single quotes
print("Roger\nDog")      # newline
print("Roger\tDog")      # tab
print("C:\\Users\\roger")  # a literal backslash

# Raw strings ignore escapes
print(r"C:\new\folder")
