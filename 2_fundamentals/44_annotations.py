# Annotations (type hints) - optional; Python does not enforce them,
# but tools like mypy and editors use them.

def increment(n: int) -> int:
    return n + 1

count: int = 0
names: list[str] = ["Roger", "Syd"]

print(increment(count))
print(increment.__annotations__)
