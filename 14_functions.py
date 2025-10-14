########################################
# def greetBasic():
#     pass  # this key word tells the computer to move to the next item even if no value is returned
#     return "Hello!"

# greet = greetBasic() # I have called my function

# print (greet)
# def greet(name, age):
#     return f"Hello, {name} ({age})!"

# greetings = greet("Azeez", 28) # calling a function with arguments

# print (greetings)

#########################################
# Default Arguments: 
# def greetWithArgs(name="Guest"):
#     print(f"Hello, {name}!")


# greetWithArgs("Hybrid D. Void")


# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)  # Output: 7


# lambda function - arguments: expression
# Example:
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8



# Variable-length Arguments: You can pass an arbitrary number of arguments using *args and **kwargs.
# *args: Collects extra positional arguments into a tuple.
# def sum_numbers(*args):
#     print(args[0])
#     return sum(args)

# print(sum_numbers(1, 2, 3))  # Output: 6
# print(sum_numbers(4, 5, 6, 7))  # Output: 22



# # **kwargs: Collects extra keyword arguments into a dictionary.
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=30)
# Output:
# name: Alice
# age: 30



# Function documentation

# def add(a, b):
#     """
#     Adds two numbers.
    
#     Parameters:
#     a (int or float): The first number.
#     b (int or float): The second number.
    
#     Returns:
#     int or float: The sum of a and b.
#     """
#     return a + b


# # A higher-order function is a function that can take other functions as arguments or return a function as a result.
# # Example:
def apply_function(func, x, y):
    return func(x, y)

result = apply_function(add, 3, 5)  # Pass `add` function as argument
print(result)  # Output: 8


# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 14_functions.py