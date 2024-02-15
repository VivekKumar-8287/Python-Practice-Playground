x = 4       # x is of type int
x = "Sally" # x is now of type str

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes
# Variable names are case-sensitive.

# Legal Variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Illegal variables
'''
2myvar = "John"
my-var = "John"
my var = "John"

'''
# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"

# And you can assign the same value to multiple variables in one line
x = y = z = "Orange"

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Output Variables
print()

# Global Variables
'''
Variables that are created outside of a function are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.
'''