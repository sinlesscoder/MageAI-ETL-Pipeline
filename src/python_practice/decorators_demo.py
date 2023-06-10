# Functions where functions are input

def func_2(func_1):
    return func_1()

def greet():
    print("Hi")


some_call = func_2(greet)

print(some_call)

# Closure
def outer_func(func_example):
    def inner():
        print("Your function is being executed.")
        example = func_example()
        print("Your function has finished executing")
        return example
    return inner

# Decorator Syntax
@outer_func
def random_add():
    return 5 + 5

print(random_add())