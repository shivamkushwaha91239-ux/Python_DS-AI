def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def floor_div(a,b):
    return a//b

def mod(a,b):
    return a%b

addition = add(10,20)
subtraction = sub(10,20)
multiplication = mul(10,20)
division = div(10,20)
floor_division = floor_div(10,20)
remainder = mod(10,20)

print("Addition of 10 and 20 is: ", addition)
print("Subtraction of 10 and 20 is: ", subtraction)
print("Multiplication of 10 and 20 is: ", multiplication)
print("Division of 10 and 20 is: ", division)
print("Floor Division of 10 and 20 is: ", floor_division)
print("Remainder of 10 and 20 is: ", remainder)


# exponent functions
def square(x):
    print(f"The square of {x} is {x**2}")
    
x = int(input("Enter a num for its square: "))
square(x)


def cube(n):
    print(f"The cube of {n} is {n**3}")

n = int(input("Enter a number for its cube: "))
cube(n)

# Lambda Functions
square = lambda x: x**2
print(square(5))

# -------------------------------------------------------------------------------
# ARGS AND KWARGS

# Positional arguments are the most common type of arguments in Python. They are passed to a function based on their position or order in the function call. The first argument is assigned to the first parameter, the second argument to the second parameter, and so on.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 25)  # Positional arguments

# Args is used to pass a variable number of arguments to a function. It allows you to pass any number of positional arguments to a function, and they are collected into a tuple.
def sum(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum(1, 2, 3, 4, 5)) 

# Keyword arguments (kwargs) are another way to pass arguments to a function. They allow you to specify the names of the parameters when calling the function, making it clear which argument corresponds to which parameter.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(name="Bob", age=30)  # Keyword arguments
greet(age=30, name="Bob")  # Keyword arguments can be in any order

# Kwargs is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of named arguments to a function, and they are collected into a dictionary.
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Charlie", age=35, city="New York")