# Decorators - wrap a function to change or extend its behavior

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello!")

hello()
