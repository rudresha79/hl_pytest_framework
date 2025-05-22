


def dec_function(func):
    def wrapper_fnctio():
        print("Wrapper executed before", func.__name__)
        func()
        print("Wrapper executed after", func.__name__)
    return wrapper_fnctio

def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level.upper()}] Executing {func.__name__} with args: {args} kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"[{level.upper()}] {func.__name__} returned: {result}")
            return result
        return wrapper
    return decorator

@log("debug")
def add(a, b):
    return a + b

@log("info")
def multiply(a, b):
    return a * b

# Example usage



@dec_function
def disppay():
    print(("Print display"))




disppay()

add(2, 3)
multiply(4, 5)