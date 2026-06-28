# ==============================
# Python Syntax
# ==============================
# Python uses indentation instead of { }.
# Each statement is usually written on a new line.
# Example:
# if condition:
#     code here

# Challenge:
"""
# Print "Hello World!"
print("Hello World!")

# Print "Have a good day."
print("Have a good day.")

# Print "Learning Python is fun!"
print("Learning Python is fun!")
"""

# ==============================
# Python Output
# ==============================
# Use print() to display output.
# Syntax:
# print("Hello")
# print(variable_name)

# Challenge:
"""
# Print "I am" and the number 25
print("I am", 25)

"""
# ==============================
# Python Comments
# ==============================
# Single-line comment starts with #
# Multi-line notes can be written using triple quotes:
# """
# This is a multi-line comment
# """


# ==============================
# Python Variables
# ==============================

# Create a variable:
# variable_name = value

# Examples:
# x = 5
# name = "Dania"
# price = 10.5
# is_active = True

# Python does not need type declaration.
# A variable is created when a value is assigned to it.

# A variable can change type:
# x = 10
# x = "Hello"

# Check variable type:
# type(x)

# Casting:
# x = str(3)      # "3"
# y = int(3)      # 3
# z = float(3)    # 3.0

# Strings can use single or double quotes:
# name = "Dania"
# name = 'Dania'

# Variable names are case-sensitive:
# age = 22
# Age = 25


# ==============================
# Variable Names
# ==============================

# Valid names:
# myvar = "Dania"
# my_var = "Dania"
# _my_var = "Dania"
# myVar = "Dania"
# MYVAR = "Dania"
# myvar2 = "Dania"

# Invalid names:
# 2myvar = "Dania"
# my-var = "Dania"
# my var = "Dania"

# Naming rules:
# Must start with a letter or underscore.
# Cannot start with a number.
# Can contain letters, numbers, and underscores.
# Cannot use Python keywords.
# Case-sensitive.

# Naming styles:
# camelCase = myVariableName
# PascalCase = MyVariableName
# snake_case = my_variable_name


# ==============================
# Assign Multiple Values
# ==============================

# Assign many values to many variables:
# x, y, z = "Orange", "Banana", "Cherry"

# Number of variables must match number of values.

# Assign one value to many variables:
# x = y = z = "Python"

# Unpack a list/tuple:
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# ==============================
# Output Variables
# ==============================

# Print one variable:
# print(x)

# Print multiple variables using commas:
# print(x, y, z)

# Commas support different data types:
# name = "Dania"
# age = 22
# print(name, age)

# Use + to concatenate strings:
# first = "Python "
# second = "is "
# third = "easy"
# print(first + second + third)

# + with numbers means addition:
# x = 5
# y = 10
# print(x + y)

# Do not concatenate string + number directly:
# print("Age: " + age)  # Error if age is int

# Use comma or casting:
# print("Age:", age)
# print("Age: " + str(age))

# ==============================
# Global Variables
# ==============================

# Global variable: created outside a function.
# Can be used inside and outside functions.

# Example:
# x = "awesome"
#
# def myfunc():
#     print("Python is " + x)
#
# myfunc()

# Local variable: created inside a function.
# It is only available inside that function.

# Same name inside function creates a local variable:
# x = "global"
#
# def test():
#     x = "local"
#     print(x)
#
# test()
# print(x)

# Use global keyword to modify a global variable inside a function:
# x = "old"
#
# def change_value():
#     global x
#     x = "new"
#
# change_value()
# print(x)

# Challenge:
"""
# Create variable x with value 5
x = 5

# Create variable y with value "John"
y = "John"

# Print the type of x
print(type(x))
"""
# ==============================
# Python Data Types
# ==============================
# Common data types:
# str  -> "Hello"
# int  -> 10
# float -> 10.5
# bool -> True / False
# list -> [1, 2, 3]
# tuple -> (1, 2, 3)
# dict -> {"name": "Rama", "age": 22}
# set -> {1, 2, 3}

# Check type:
# type(variable)

# Challenge:
"""
# Create variables
x = 5
y = 3.14
z = "Hello"

# Print the data type of each variable
print(type(x))
print(type(y))
print(type(z))
"""
# ==============================
# Python Numbers
# ==============================
# int: whole numbers
# x = 10
# float: decimal numbers
# y = 3.5
# complex:
# z = 2 + 3j

# Convert numbers:
# int(3.5)
# float(5)

# Challenge:
"""
# Create an integer
x = 5

# Create a float
y = 3.14

# Create a complex number
z = 2+3j

# Print the types
print(type(x))
print(type(y))
print(type(z))
"""

# ==============================
# Python Casting
# ==============================
# Casting means converting from one type to another.
# Syntax:
# int(value)
# float(value)
# str(value)

# Examples:
# x = int("5")
# y = str(10)
# z = float(3)

# Challenge:
"""
# Create an integer
x = 1

# Convert to float
a = float(x)

# Convert to string
b = str(x)

# Print values
print(a)
print(b)
"""

# ==============================
# Python Strings
# ==============================

# String syntax:
# name = "Dania"
# name = 'Dania'

# Multiline string:
# text = """Hello
# Python"""

# Access characters by index:
# name = "Dania"
# name[0]   # D
# name[1]   # a

# Negative index:
# name[-1]  # a

# String length:
# len(name)

# Check if text exists:
# "Da" in name
# "x" not in name

# Challenge:
# Create a string with your name.
# Print the first character, last character, and length.


# ==============================
# Slicing Strings
# ==============================

# Syntax:
# string[start:end]
# end is not included.

# Examples:
# name = "Dania"
# name[0:3]    # Dan
# name[:3]     # Dan
# name[2:]     # nia
# name[-3:-1]  # ni

# ==============================
# Modify Strings
# ==============================

# Convert to uppercase:
# name.upper()

# Convert to lowercase:
# name.lower()

# Remove spaces from start/end:
# text.strip()

# Replace characters/words:
# name.replace("a", "o")

# Split string into list:
# sentence.split(" ")

# Examples:
# name = " Dania "
# name.strip() Dania
# name.upper() DANIA
# name.lower() dania

# ==============================
# Concatenate Strings
# ==============================

# Use + to join strings:
# first = "Dania"
# last = "Ahmad"
# full_name = first + " " + last

# Use comma in print:
# print(first, last)

# Cannot directly join string + number:
# print("Age: " + 22)  # Error

# Correct:
# print("Age:", 22)
# print("Age: " + str(22))

# ==============================
# Format Strings
# ==============================

# f-string syntax:
# name = "Dania"
# age = 22
# text = f"My name is {name} and I am {age} years old"

# Expressions inside f-string:
# price = 10
# text = f"Total: {price * 2}"

# Format decimal:
# price = 9.567
# text = f"Price: {price:.2f}"

# ==============================
# Escape Characters
# ==============================

# Escape character starts with backslash \

# New line:
# print("Hello\nDania")

# Tab:
# print("Hello\tDania")

# Double quote inside string:
# print("My name is \"Dania\"")

# Backslash:
# print("C:\\Users\\Dania")

# ==============================
# String Methods
# ==============================

# Common string methods:
# name.upper()
# name.lower()
# name.strip()
# name.replace("a", "o")
# name.split(" ")
# name.capitalize()
# name.title()
# name.count("a")
# name.find("n")
# name.startswith("D")
# name.endswith("a")

# Example:
# name = "dania"
# name.capitalize()  # Dania

# Challenge:
"""
# Create the variable
txt = "Hello, World!"

# Print characters from index 2 to 5
print(txt[2:5])

# Print in upper case
print(txt.upper())

# Create the name variable
name = "Python"

# Print using an f-string
print(f"I love {name}")
"""
# ==============================
# Python Booleans
# ==============================
# Boolean values:
# True
# False

# Used in conditions:
# x = 5
# print(x > 3)   # True
# print(x == 10) # False

# Challenge:
"""
# Print the result of 10 > 9
print(10 > 9)

# Print the result of 10 == 9
print(10 == 9)

# Print the result of bool("Hello")
print(bool("Hello"))

# Print the result of bool(0)
print(bool(0))
"""
# ==============================
# Python Operators
# ==============================
# Arithmetic:
# +  -  *  /  %  **  //

# Comparison:
# ==  !=  >  <  >=  <=

# Logical:
# and  or  not

# Assignment:
# =  +=  -=  *=  /=

# Example:
# x = 5
# x += 2

# Challenge:
"""
# Create variables
a = 15
b = 4

# Print modulus
print(a % b)

# Print floor division
print(a // b)

# Print power
print(a ** b)

# Add 10 to a
a += 10
print(a)
"""

# ==============================
# Python Lists
# ==============================

# Create a list:
# list_name = [item1, item2, item3]

# Example:
# colors = ["red", "green", "blue"]

# Lists are:
# Ordered
# Changeable
# Allow duplicate values


# ==============================
# Access List Items
# ==============================

# Access by index:
# colors[0]   # first item
# colors[1]   # second item

# Negative index:
# colors[-1]  # last item

# Range:
# colors[0:2] # items from index 0 to 1


# ==============================
# Change List Items
# ==============================

# Change item by index:
# colors[1] = "yellow"

# Change a range:
# colors[0:2] = ["black", "white"]


# ==============================
# Add List Items
# ==============================

# Add item to the end:
# colors.append("purple")

# Add item at specific index:
# colors.insert(1, "orange")

# Add another list:
# colors.extend(["pink", "gray"])


# ==============================
# Remove List Items
# ==============================

# Remove by value:
# colors.remove("red")

# Remove by index:
# colors.pop(0)

# Remove last item:
# colors.pop()

# Delete item:
# del colors[0]

# Clear all items:
# colors.clear()


# ==============================
# Loop Lists
# ==============================

# Loop through items:
# for color in colors:
#     print(color)

# Loop using index:
# for i in range(len(colors)):
#     print(colors[i])


# ==============================
# List Comprehension
# ==============================

# Short way to create a new list:
# new_list = [item for item in list if condition]

# Example:
# long_colors = [color for color in colors if len(color) > 4]


# ==============================
# Sort Lists
# ==============================

# Sort ascending:
# colors.sort()

# Sort descending:
# colors.sort(reverse=True)

# Reverse current order:
# colors.reverse()

# Sort using key:
# numbers.sort(key=my_function)


# ==============================
# Copy Lists
# ==============================

# Correct copy:
# new_colors = colors.copy()

# Another way:
# new_colors = list(colors)

# Avoid:
# new_colors = colors
# Because both variables will point to the same list.


# ==============================
# Join Lists
# ==============================

# Join using +:
# list3 = list1 + list2

# Join using extend:
# list1.extend(list2)


# ==============================
# List Methods
# ==============================

# append()   -> add item to end
# insert()   -> add item at index
# extend()   -> add another list
# remove()   -> remove by value
# pop()      -> remove by index
# clear()    -> remove all items
# sort()     -> sort list
# reverse()  -> reverse order
# copy()     -> copy list
# count()    -> count item occurrences
# index()    -> get item index

# Code Challenge:
"""
# Create a list
colors = ["red", "green", "blue"]

# Print the first item
print(colors[0])

# Change the second item to "yellow"
colors[1] = "yellow"

# Add "purple" to the end
colors.append("purple")

# Remove "red"
colors.remove("red")

# Print the list
print(colors)
"""

# ==============================
# Python Tuples
# ==============================

# Create a tuple:
# tuple_name = (item1, item2, item3)

# Example:
# fruits = ("apple", "banana", "cherry")

# Tuples are:
# Ordered
# Unchangeable
# Allow duplicate values

# Tuple with one item:
# item = ("apple",)
# The comma is required.


# ==============================
# Access Tuples
# ==============================

# Access by index:
# fruits[0]   # first item
# fruits[1]   # second item

# Negative index:
# fruits[-1]  # last item

# Range:
# fruits[0:2] # items from index 0 to 1


# ==============================
# Update Tuples
# ==============================

# Tuples cannot be changed directly.

# To update a tuple:
# Convert tuple to list
# Change the list
# Convert it back to tuple

# Example:
# fruits = ("apple", "banana", "cherry")
# temp = list(fruits)
# temp[1] = "kiwi"
# fruits = tuple(temp)


# ==============================
# Unpack Tuples
# ==============================

# Unpack tuple values into variables:
# fruits = ("apple", "banana", "cherry")
# a, b, c = fruits

# print(a)  # apple
# print(b)  # banana
# print(c)  # cherry

# Use * for remaining items:
# fruits = ("apple", "banana", "cherry", "orange")
# a, b, *c = fruits


# ==============================
# Loop Tuples
# ==============================

# Loop through items:
# for fruit in fruits:
#     print(fruit)

# Loop using index:
# for i in range(len(fruits)):
#     print(fruits[i])


# ==============================
# Join Tuples
# ==============================

# Join using +:
# tuple3 = tuple1 + tuple2

# Repeat tuple:
# fruits = ("apple", "banana")
# repeated = fruits * 2


# ==============================
# Tuple Methods
# ==============================

# count() -> count how many times a value appears
# index() -> return the index of a value

# Example:
# numbers = (1, 2, 2, 3)
# numbers.count(2)  # 2
# numbers.index(3)  # 3

# Code Challenge:
"""
# Create the tuple
fruits = ("apple", "banana", "cherry")

# Print the second item
print(fruits[1])

# Print the number of items
print(len(fruits))

# Unpack the tuple
(a, b, c) = fruits

# Print b
print(b)
"""

# ==============================
# Python Sets
# ==============================

# Create a set:
# set_name = {item1, item2, item3}

# Example:
# colors = {"red", "green", "blue"}

# Sets are:
# Unordered
# Unchangeable items
# Do not allow duplicate values

# Note:
# You cannot access set items by index.


# ==============================
# Access Set Items
# ==============================

# Sets do not have indexes.
# Access items using a loop:
# for color in colors:
#     print(color)

# Check if item exists:
# "red" in colors


# ==============================
# Add Set Items
# ==============================

# Add one item:
# colors.add("yellow")

# Add items from another set/list/tuple:
# colors.update(["pink", "black"])


# ==============================
# Remove Set Items
# ==============================

# Remove item:
# colors.remove("red")
# remove() gives an error if item does not exist.

# Remove item safely:
# colors.discard("red")
# discard() does not give an error if item does not exist.

# Remove random item:
# colors.pop()

# Clear all items:
# colors.clear()

# Delete set:
# del colors


# ==============================
# Loop Sets
# ==============================

# Loop through set items:
# for color in colors:
#     print(color)


# ==============================
# Join Sets
# ==============================

# union() returns a new set:
# set3 = set1.union(set2)

# update() adds items to the original set:
# set1.update(set2)

# intersection() keeps common items:
# set3 = set1.intersection(set2)

# difference() keeps items only in the first set:
# set3 = set1.difference(set2)

# symmetric_difference() keeps items not common in both sets:
# set3 = set1.symmetric_difference(set2)


# ==============================
# Frozenset
# ==============================

# frozenset is like set, but cannot be changed.
# You cannot add or remove items.

# Example:
# colors = frozenset({"red", "green", "blue"})


# ==============================
# Set Methods
# ==============================

# add()        -> add one item
# update()     -> add multiple items
# remove()     -> remove item, error if not found
# discard()    -> remove item, no error if not found
# pop()        -> remove random item
# clear()      -> remove all items
# union()      -> join sets
# intersection() -> common items
# difference() -> items only in first set
# copy()       -> copy set


# Code Challenge:
"""
# Create the set
colors = {"red", "green", "blue"}

# Print the set
print(colors)

# Add "yellow"
colors.add("yellow")

# Remove "green"
colors.discard("green")

# Print the number of items
print(len(colors))
"""

# ==============================
# Python Dictionaries
# ==============================

# Create a dictionary:
# dict_name = {
#     "key1": value1,
#     "key2": value2
# }

# Example:
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2024
# }

# Dictionaries are:
# Ordered
# Changeable
# Do not allow duplicate keys

# Data is stored as key-value pairs.


# ==============================
# Access Items
# ==============================

# Access value by key:
# car["model"]

# Another way:
# car.get("model")

# Get all keys:
# car.keys()

# Get all values:
# car.values()

# Get all key-value pairs:
# car.items()


# ==============================
# Change Items
# ==============================

# Change value by key:
# car["year"] = 2025

# Update dictionary:
# car.update({"year": 2025})


# ==============================
# Add Items
# ==============================

# Add new key-value pair:
# car["color"] = "red"

# Add using update:
# car.update({"color": "red"})


# ==============================
# Remove Items
# ==============================

# Remove by key:
# car.pop("brand")

# Remove last inserted item:
# car.popitem()

# Delete by key:
# del car["model"]

# Clear dictionary:
# car.clear()


# ==============================
# Loop Dictionaries
# ==============================

# Loop through keys:
# for key in car:
#     print(key)

# Loop through values:
# for value in car.values():
#     print(value)

# Loop through keys and values:
# for key, value in car.items():
#     print(key, value)


# ==============================
# Copy Dictionaries
# ==============================

# Correct copy:
# new_car = car.copy()

# Another way:
# new_car = dict(car)

# Avoid:
# new_car = car
# Because both variables will point to the same dictionary.


# ==============================
# Nested Dictionaries
# ==============================

# Dictionary inside dictionary:
# students = {
#     "student1": {
#         "name": "Dania",
#         "age": 22
#     },
#     "student2": {
#         "name": "Sara",
#         "age": 21
#     }
# }

# Access nested value:
# students["student1"]["name"]


# ==============================
# Dictionary Methods
# ==============================

# get()       -> get value by key
# keys()      -> return all keys
# values()    -> return all values
# items()     -> return key-value pairs
# update()    -> update/add items
# pop()       -> remove item by key
# popitem()   -> remove last inserted item
# clear()     -> remove all items
# copy()      -> copy dictionary


# Code Challenge:
"""
# Create the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}

# Print the model
print(car["model"])

# Add a color key
car["color"] = "red"

# Remove the brand key
car.pop("brand")

# Print the dictionary
print(car)
"""

# ==============================
# Python If...Else
# ==============================

# if is used to run code only when a condition is True.

# Basic syntax:
# if condition:
#     code

# Example:
# age = 20
# if age >= 18:
#     print("Adult")

# Python uses indentation to define the if block.


# ==============================
# Python If
# ==============================

# if checks one condition.

# Example:
# x = 10
# if x > 5:
#     print("x is greater than 5")


# ==============================
# Python Elif
# ==============================

# elif means "else if".
# Used to check another condition if the first one is False.

# Example:
# grade = 80
# if grade >= 90:
#     print("Excellent")
# elif grade >= 70:
#     print("Good")


# ==============================
# Python Else
# ==============================

# else runs if all previous conditions are False.

# Example:
# age = 15
# if age >= 18:
#     print("Adult")
# else:
#     print("Not adult")


# ==============================
# Shorthand If
# ==============================

# One-line if:
# if condition: code

# Example:
# if age > 18: print("Adult")

# One-line if else:
# result = "Adult" if age >= 18 else "Minor"

# Example:
# status = "Pass" if grade >= 50 else "Fail"


# ==============================
# Logical Operators
# ==============================

# and -> both conditions must be True
# or  -> at least one condition must be True
# not -> reverses the condition

# Example:
# age = 20
# has_id = True
#
# if age >= 18 and has_id:
#     print("Allowed")

# Example:
# if age < 18 or has_id == False:
#     print("Not allowed")


# ==============================
# Nested If
# ==============================

# Nested if means if inside another if.

# Example:
# age = 20
# has_id = True
#
# if age >= 18:
#     if has_id:
#         print("Allowed")
#     else:
#         print("ID required")


# ==============================
# Pass Statement
# ==============================

# pass is used when a block cannot be empty.
# It does nothing.

# Example:
# if age > 18:
#     pass


# Code Challenge:
"""
# Create age variable
age = 20

# Write if/elif/else
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
"""

# ==============================
# Python Match
# ==============================

# match is used to compare a value with different cases.
# It is similar to switch in other programming languages.

# Basic syntax:
# match variable:
#     case value1:
#         code
#     case value2:
#         code
#     case _:
#         default code

# case _ means default case.
# It runs if no other case matches.

# Example:
# day = 1
#
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Other day")


# ==============================
# Multiple Values in One Case
# ==============================

# Use | to match more than one value.

# Example:
# day = 6
#
# match day:
#     case 6 | 7:
#         print("Weekend")
#     case _:
#         print("Weekday")


# ==============================
# Match with Strings
# ==============================

# match can be used with strings too.

# Example:
# role = "admin"
#
# match role:
#     case "admin":
#         print("Full access")
#     case "user":
#         print("Limited access")
#     case _:
#         print("Unknown role")


# Code Challenge:
"""
# Create variable day
day = 3

# Use match statement
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")
"""

# ==============================
# Python While Loop
# ==============================

# while repeats code as long as the condition is True.

# Basic syntax:
# while condition:
#     code

# Example:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# Important:
# Update the variable inside the loop to avoid infinite loop.

# break    -> stops the loop
# continue -> skips the current iteration and goes to the next one
# else     -> runs when the loop finishes normally

# Code Challenge:
"""
# Create the i variable
i = 0

# While loop: print 1-5, skip 3 with continue
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
"""

# ==============================
# Python For Loops
# ==============================

# for loop repeats code for each item in a sequence.

# Basic syntax:
# for variable in sequence:
#     code

# Example:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# Loop through a string:
# for letter in "Dania":
#     print(letter)

# break -> stops the loop
# continue -> skips current iteration and continues with the next one

# range() -> used to loop a specific number of times
# for i in range(5):
#     print(i)

# range(start, end):
# for i in range(1, 6):
#     print(i)

# else with for:
# for x in range(3):
#     print(x)
# else:
#     print("Loop finished")

# Nested loop:
# for x in list1:
#     for y in list2:
#         print(x, y)

# pass -> placeholder when the loop body is empty
# for x in fruits:
#     pass

# Code Challenge:
"""
# Create the fruits list
fruits = ["apple", "banana", "cherry"]

# Loop through fruits, break at "banana"
for x in fruits:
    print(x)
    if x == "banana":
        break
"""

# ==============================
# Python Functions
# ==============================

# Function is a block of code that runs when called.

# Basic syntax:
# def function_name():
#     code

# Example:
# def greet():
#     print("Hello")

# Call function:
# greet()


# ==============================
# Python Arguments
# ==============================

# Arguments are values passed to a function.

# Syntax:
# def function_name(parameter):
#     code

# Example:
# def greet(name):
#     print("Hello " + name)

# greet("Dania")


# ==============================
# Python *args
# ==============================

# *args allows passing many arguments.
# It stores them as a tuple.

# Example:
# def print_names(*names):
#     print(names[0])

# print_names("Dania", "Sara", "Lana")


# ==============================
# Python **kwargs
# ==============================

# **kwargs allows passing key-value arguments.
# It stores them as a dictionary.

# Example:
# def student_info(**student):
#     print(student["name"])

# student_info(name="Dania", age=22)


# ==============================
# Python Scope
# ==============================

# Local variable: created inside a function.
# Global variable: created outside a function.

# Example:
# x = "global"

# def myfunc():
#     y = "local"
#     print(y)

# myfunc()


# ==============================
# Python Decorators
# ==============================

# Decorator is a function that modifies another function.

# Basic syntax:
# @decorator_name
# def function_name():
#     code

# Simple example:
# def my_decorator(func):
#     def wrapper():
#         print("Before")
#         func()
#         print("After")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")


# ==============================
# Python Lambda
# ==============================

# lambda is a small anonymous function.

# Syntax:
# lambda arguments: expression

# Example:
# square = lambda x: x * x
# print(square(5))


# ==============================
# Python Recursion
# ==============================

# Recursion means a function calls itself.

# Example:
# def countdown(n):
#     if n > 0:
#         print(n)
#         countdown(n - 1)

# countdown(3)


# ==============================
# Python Generators
# ==============================

# Generator uses yield instead of return.
# It gives values one by one.

# Example:
# def numbers():
#     yield 1
#     yield 2
#     yield 3

# for num in numbers():
#     print(num)

# Code Challenge:

"""
# Create the greet function
def greet(name):
    print("Hello, " + name)

# Call greet
greet("Emil")
"""

# ==============================
# Python range()
# ==============================

# range() creates an immutable sequence of numbers.
# Mostly used with for loops.

# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# stop is not included.

# Examples:
# range(6)        -> 0, 1, 2, 3, 4, 5
# range(2, 6)     -> 2, 3, 4, 5
# range(2, 10, 2) -> 2, 4, 6, 8

# Convert range to list:
# list(range(5))

# Check if value exists:
# 3 in range(5)

# Get length:
# len(range(5))

# Code Challenge:
"""
# Print 0 through 5
for x in range(6):
    print(x)

# Print 2 through 5
for x in range(2, 6):
    print(x)
"""
# array in python same lists
"""
# Create a list
cars = ["Ford", "Volvo", "BMW"]

# Print the first item
print(cars[0])

# Change the second item to "Toyota"
cars[1] = "Toyota"

# Print the list
print(cars)
"""

# ==============================
# Python Iterators
# ==============================

# Iterator: object used to go through values one by one.

# Iterator protocol:
# __iter__()  -> returns the iterator object
# __next__()  -> returns the next item

# iter() creates an iterator from an iterable.
# next() gets the next value.

# Iterable examples:
# list, tuple, set, dictionary, string

# Example:
# fruits = ("apple", "banana", "cherry")
# myit = iter(fruits)
# print(next(myit))  # apple
# print(next(myit))  # banana

# Strings are iterable:
# text = "Dania"
# myit = iter(text)
# print(next(myit))  # D

# for loop automatically uses iter() and next().

# StopIteration:
# Used to stop the iterator when there are no more values.


# ==============================
# Create Custom Iterator
# ==============================

# To create an iterator inside a class:
# Use __iter__() and __next__()

# Example:
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# Code Challenge:
"""
# Create a tuple
mytuple = ("apple", "banana", "cherry")

# Create an iterator
myit = iter(mytuple)

# Print the first item
print(next(myit))
"""

# ==============================
# Python Modules
# ==============================

# Module: a .py file that contains reusable code.

# Import a module:
# import module_name

# Use something from module:
# module_name.function_name()

# Example:
# import mymodule
# mymodule.greeting("Dania")

# Rename module:
# import mymodule as mx

# Import specific item:
# from mymodule import person1
# print(person1["age"])

# Built-in module example:
# import platform
# print(platform.system())

# dir() shows names inside a module:
# print(dir(platform))

# Code Challenge:
"""
# Import the platform module
import platform

# Print the system platform
print(platform.system())
"""
# ==============================
# Python Dates
# ==============================

# Python does not have a built-in date data type.
# Use datetime module to work with dates and times.

# Import datetime:
# import datetime

# Get current date and time:
# x = datetime.datetime.now()

# Access date parts:
# x.year
# x.month
# x.day
# x.hour
# x.minute
# x.second

# Create specific date:
# x = datetime.datetime(2024, 6, 28)

# Format date using strftime():
# x.strftime("%A")  # weekday name
# x.strftime("%B")  # month name
# x.strftime("%Y")  # full year

# Code Challenge:
"""
# Import the datetime module
import datetime

# Store the current date and time in x
x = datetime.datetime.now()

# Print the year
print(x.year)
"""
# ==============================
# Python Math
# ==============================

# Built-in math functions:
# min() -> lowest value
# max() -> highest value
# abs() -> positive value
# pow(x, y) -> x to the power of y

# Math module:
# import math

# Common math module functions:
# math.sqrt(x)   -> square root
# math.ceil(x)   -> round up
# math.floor(x)  -> round down
# math.pi        -> PI value

# Code Challenge:
"""
# Print the lowest value
print(min(5, 10))

# Print the highest value
print(max(5, 10))

# Print the absolute value
print(abs(-7.25))

# Print 4 to the power of 3
print(pow(4, 3))
"""
# ==============================
# Python JSON
# ==============================

# JSON is used to store and exchange data.
# Python has a built-in json module.

# Import json:
# import json

# Convert JSON string to Python dictionary:
# json.loads(json_string)

# Convert Python object to JSON string:
# json.dumps(python_object)

# Pretty format JSON:
# json.dumps(data, indent=4)

# Sort JSON keys:
# json.dumps(data, sort_keys=True)

# Code Challenge:
"""
# Import json
import json

# Create a JSON string
x = '{"name": "Emil", "age": 30}'

# Parse the JSON string
y = json.loads(x)

# Print the age
print(y["age"])
"""
# ==============================
# Python RegEx
# ==============================

# RegEx: a search pattern used to find/check text.
# Python uses the re module.

# Import re:
# import re

# Main functions:
# re.search()  -> finds first match
# re.findall() -> returns all matches as a list
# re.split()   -> splits string by pattern
# re.sub()     -> replaces matches

# Common patterns:
# ^   -> starts with
# $   -> ends with
# .   -> any character
# *   -> zero or more
# +   -> one or more
# \d  -> digit
# \s  -> whitespace
# \w  -> word character
# []  -> set of characters

# Match object methods:
# x.span()   -> start and end position
# x.group()  -> matched text
# x.string   -> original string

# Code Challenge:
"""
# Import re
import re

# Create a string
txt = "The rain in Spain"

# Search for "Spain"
x = re.search("Spain", txt)

# Print the span
print(x.span())
"""
# ==============================
# Python Try Except
# ==============================

# try     -> test code for errors
# except  -> handle the error
# else    -> runs if no error happens
# finally -> runs always

# Basic syntax:
# try:
#     code
# except:
#     code if error happens

# Specific exception:
# except NameError:
#     print("Variable not defined")

# Raise error manually:
# raise Exception("Error message")


# ==============================
# Python PIP
# ==============================

# PIP is Python's package manager.
# Used to install, uninstall, and list packages.

# Check pip version:
# pip --version

# Install package:
# pip install package_name

# Uninstall package:
# pip uninstall package_name

# List installed packages:
# pip list

# Use installed package:
# import package_name

# Code Challenge:
"""
# Try to print x
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("Execution complete")
"""
# ==============================
# Python String Formatting
# ==============================

# f-string is the preferred way to format strings.
# Add f before the string.

# Syntax:
# f"Text {variable}"

# Example:
# name = "Dania"
# txt = f"Hello {name}"

# Placeholders can contain:
# variables
# operations
# functions

# Examples:
# f"The price is {price}"
# f"Total is {20 * 5}"
# f"Name: {name.upper()}"

# Format decimals:
# f"{price:.2f}"   # 2 decimal places

# Thousand separator:
# f"{price:,}"

# Old way:
# "Hello {}".format(name)

# Code Challenge:
"""
# Create a variable
price = 49

# Create an f-string
txt = f"The price is {price} dollars"

# Print the result
print(txt)
"""
# ==============================
# Python None
# ==============================

# None means no value / not set.
# Its type is NoneType.

# Assign None:
# x = None

# Check type:
# type(x)

# Compare with None:
# x is None
# x is not None

# None is False in boolean context:
# bool(None)  # False

# A function without return returns None.

# Code Challenge:
"""
# Assign None to x
x = None

# Check if x is None
if x is None:
    print("x is None")
"""
# ==============================
# Python User Input
# ==============================

# input() is used to take data from the user.

# Basic syntax:
# name = input()

# With prompt:
# name = input("Enter your name: ")

# Input is always stored as a string.

# Convert input to number:
# age = int(input("Enter your age: "))
# price = float(input("Enter price: "))

# Multiple inputs:
# name = input("Enter name: ")
# age = input("Enter age: ")

# Validate input using try/except.

# ==============================
# Python Virtual Environment
# ==============================

# Virtual environment: isolated environment for a Python project.
# Each project can have its own Python version and packages.

# Benefits:
# Avoid package conflicts
# Keep system Python clean
# Make projects easier to share and reproduce

# Create virtual environment:
# python -m venv myfirstproject

# Activate on Windows:
# myfirstproject\Scripts\activate

# After activation, install packages inside it:
# pip install package_name

# Example:
# pip install cowsay

# Use installed package:
# import cowsay

# Deactivate virtual environment:
# deactivate

# Delete virtual environment:
# Delete the environment folder
# or on Windows:
# rmdir /s /q myfirstproject
