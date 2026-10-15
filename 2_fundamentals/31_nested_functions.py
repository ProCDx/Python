# Nested Functions - a function defined inside another function

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(" ")
    for word in words:
        say(word)

talk("I am going to buy the milk")

# 'nonlocal' lets an inner function modify an outer function's variable
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()
