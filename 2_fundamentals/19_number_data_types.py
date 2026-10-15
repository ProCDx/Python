# Number Data Types: int, float, complex
age = 8
fraction = 0.1
complex_number = 2 + 3j

print(type(age), type(fraction), type(complex_number))
print(int("20"), float("0.5"), complex(2, 3))

print(complex_number.real, complex_number.imag)

# Big integers are fine in Python
print(2 ** 100)

# Underscores for readability
million = 1_000_000
print(million)
