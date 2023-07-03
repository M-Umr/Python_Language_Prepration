def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  #calling say_hello('John') and result will be Hello, John!
        return result.upper()  # return HELLO, JOHN!
    return wrapper

@uppercase_decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("John"))
