'''
# What is a Module?
A module is a file containing Python definitions and statements. It can include:
 ->    Functions
 ->	   Variables
 ->    Classes
 ->    Imports of other modules

Modules allow you to organize your code into logical sections, making it reusable and easier to manage.
'''

'''# How to Import a Module

# There are three types of modules - built-in modules, third-party modules and custom modules
# Built-in modules are the ones built into Python directly. You do not have to install them or write them yourself.
# Third-party modules are modules written by other developers to make work easier. 
  They made available for others to install from https://pypi.org
# Custom modules are the ones you wrote yourself for different implementations in your codebase
'''


# To use a module, you can import it:

import math

# print(math.sqrt(16))  # Using the math module to find the square root

# x = math.ceil(2.4)
# y = math.floor(2.4)


# print(x) # returns 3
# print(y) # returns 2 

###### Date and time module
# import datetime

# a = datetime.datetime.now()
# print(a) 

# b = datetime.datetime(2020, 5, 17)

# print(b) 


# # You can also import specific functions or variables from a module:
# from math import pi

# print(pi)  # Direct access to pi



'''
# Built-in Modules
# Python includes a variety of built-in modules that you can import to extend the functionality of your code.

# Some common built-in modules include:
# ->    math: Provides mathematical functions like sqrt(), factorial(). (https://www.w3schools.com/python/module_math.asp)
# ->    os: Provides functions for interacting with the operating system (e.g., file manipulation, working with directories).
# ->    datetime: Provides functions for working with dates and times. (https://www.w3schools.com/python/python_datetime.asp)
#->     logging: Provides functions for logging executions, actions, exceptions, and etc
'''

# Example:
# import os

# print(os.listdir())  # List files and directories in the current directory


'''
What is a Package?
A package is a collection of modules in a directory. 
It must include a special file called __init__.py, which can be empty or include initialization code for the package.

Structure of a Package:
my_package/
    __init__.py
    module1.py
    module2.py
'''


# To import a module from a package:
# from my_package import module1


# # renaming an import
# import mymodule as mx

# a = mx.person1["age"]
# print(a) 


# Creating a custom module circle.py
# circle.py - we have the following in the circle.py file
# import math

# def area(radius):
#     return math.pi * radius ** 2

# Let us create a script that imports and uses circle.py 
import circle

radius = 5
area = circle.area(radius)
shape = circle.shape()
print(f"The area of the {shape} with radius {radius} is {area}")


# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 20_modules.py
