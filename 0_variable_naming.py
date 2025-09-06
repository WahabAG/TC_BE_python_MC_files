# Variables Naming Criteria

# must begin with a letter or underscore
# cannot start with a number
# Can only contain alphabets, numbers, and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (name, Name and NAME are three different variables)
# cannot be any of the Python keywords.
# ensure that your variables are descriptive enough


myvariable = "Alice"
my_variable = "Alice"
_my_variable = "Alice"
myVariable = "Alice"
MYVARIABLE = "Alice"
myvariable2 = "Alice"

# Outputting variables
a, b, c = "John", "James", "Jane"

print(a)
print(b)
print(c)
print(a, b, c)

print(a + b + c)
print(a +" "+ b + " " + c)
print("My name is "+ a +", His name is "+ b +" and Her name is "+ c)

print(f"My name is {a}, His Name is {b}, and Her name is {c}")

x = 2
y = 4
print(x + y)


print(x + a)    # This will not work because they are different data types
print(x, a)

# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 0_variable_naming.py