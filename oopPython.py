# ==============================
# Python OOP
# ==============================

# OOP = Object-Oriented Programming.
# It organizes code using classes and objects.

# Class: blueprint/template for creating objects.
# Object: instance created from a class.

# Benefits:
# Organized code
# Reusable code
# Easier to maintain
# Follows DRY principle


# ==============================
# Classes and Objects
# ==============================

# Create a class:
# class ClassName:
#     code

# Create an object:
# object_name = ClassName()

# __init__() runs automatically when object is created.
# self refers to the current object.

# Properties:
# self.name = name

# Methods:
# functions inside a class

# Delete object:
# del object_name

# Empty class:
# class Person:
#     pass

# Code Challenge:
"""
# Create a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

# Create an object
p1 = Person("John", 36)

# Call the method
p1.greet()
"""
# ==============================
# Python __init__() Method
# ==============================

# __init__() is a special method inside a class.
# It runs automatically when an object is created.

# Used to give initial values to object properties.

# Syntax:
# class ClassName:
#     def __init__(self, parameter1, parameter2):
#         self.property1 = parameter1
#         self.property2 = parameter2

# self refers to the current object.

# Example:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Create object:
# p1 = Person("Dania", 22)

# Access properties:
# print(p1.name)
# print(p1.age)

# Default value:
# def __init__(self, name, age=18):

# __init__() can have many parameters.

# Code Challenge:
"""
# Create the Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()
"""
# ==============================
# Python self Parameter
# ==============================

# self refers to the current object.
# It is used to access properties and methods inside the class.

# self must be the first parameter in class methods.

# Syntax:
# class ClassName:
#     def __init__(self, property):
#         self.property = property
#
#     def method_name(self):
#         print(self.property)

# Example:
# self.brand means the brand value of this specific object.

# Note:
# It can have another name, but using self is the standard convention.

# self can also be used to call another method inside the same class:
# self.method_name()

# Code Challenge:
"""
# Create the Car class
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)

# Create an object
c1 = Car("Ford")

# Call the show method
c1.show()
"""
# ==============================
# Python Class Properties
# ==============================

# Properties are variables that belong to an object or class.

# Instance properties:
# Created inside __init__().
# Each object has its own values.

# Syntax:
# class ClassName:
#     def __init__(self, property1, property2):
#         self.property1 = property1
#         self.property2 = property2

# Access property:
# object_name.property

# Modify property:
# object_name.property = new_value

# Delete property:
# del object_name.property

# Add new property to one object:
# object_name.new_property = value


# ==============================
# Class vs Object Properties
# ==============================

# Class property:
# Defined outside methods.
# Shared by all objects.

# Example:
# class Person:
#     species = "Human"   # class property
#
#     def __init__(self, name):
#         self.name = name # instance property

# Code Challenge:
"""
# Create the Student class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Create an object
s1 = Student("Anna", "A")

# Print the grade
print(s1.grade)

# Change the grade
s1.grade = "B"

# Print the updated grade
print(s1.grade)
"""
# ==============================
# Python Class Methods
# ==============================

# Methods are functions inside a class.
# They describe the behavior of objects.

# self must be the first parameter in object methods.

# Syntax:
# class ClassName:
#     def method_name(self):
#         code

# Call method:
# object_name.method_name()

# Methods can:
# Access object properties using self
# Modify object properties
# Take parameters
# Return values

# Example:
# def greet(self):
#     print(self.name)

# Method with parameters:
# def add(self, a, b):
#     return a + b

# Method returning value:
# def area(self):
#     return self.width * self.height

# __str__() controls what prints when printing the object:
# def __str__(self):
#     return "text"

# Code Challenge:
"""
# Create the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create an object
r1 = Rectangle(5, 3)

# Print the area
print(r1.area())
"""
# ==============================
# Python Inheritance
# ==============================

# Inheritance allows a class to use properties and methods
# from another class.

# Parent class: the class being inherited from.
# Child class: the class that inherits.

# Syntax:
# class ChildClass(ParentClass):
#     pass

# pass means no extra code for now.

# Child class can use parent methods and properties.

# super() is used to call the parent class __init__().

# Example:
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# Child class can also add new properties and methods.

# Code Challenge:
"""
# Create the Animal class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

# Create the Dog class (inherits from Animal)
class Dog(Animal):
    pass

# Create an object
d1 = Dog("Rex")

# Call the speak method
d1.speak()
"""
# ==============================
# Python Encapsulation
# ==============================

# Encapsulation means protecting data inside a class.
# It controls how properties are accessed or modified.

# Public property:
# self.name

# Protected property:
# self._salary
# Can be accessed, but should be treated as internal use.

# Private property:
# self.__age
# Cannot be accessed directly from outside the class.

# Getter method:
# Used to read a private value.

# Setter method:
# Used to update a private value, usually with validation.

# Example:
# def get_age(self):
#     return self.__age
#
# def set_age(self, age):
#     if age > 0:
#         self.__age = age

# Private method:
# def __validate(self):
#     code

# Name mangling:
# __age becomes _ClassName__age internally.
# Not recommended to access it this way.

# Code Challenge:
"""
# Create the ScoreBoard class
class ScoreBoard:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


# Create an object
s1 = ScoreBoard(0)

# Print the score
print(s1.get_score())
"""
# ==============================
# Python Inner Classes
# ==============================

# Inner class: a class defined inside another class.
# Used to group related/helper classes together.

# Syntax:
# class Outer:
#     class Inner:
#         code

# Create outer object:
# outer = Outer()

# Create inner object:
# inner = outer.Inner()

# Inner class does not automatically access outer object.
# To access outer data, pass outer object to inner class.

# Example:
# inner = outer.Inner(outer)

# A class can have multiple inner classes.

# Code Challenge:
"""
# Create the Car class
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = self.Engine()

    # Create inner class
    class Engine:
        def start(self):
            print("Engine started")

# Create an object
c1 = Car("Toyota")

# Call the inner class method
c1.engine.start()
"""

# ==============================
# OOP Full Challenge
# ==============================
# Create a parent class called Person.

# Person should have:
# - private property __name
# - private property __age
# - __init__ method to set name and age
# - get_name() method
# - get_age() method
# - set_age(age) method
#   The age should only change if it is greater than 0
# - introduce() method
#   It should print: "Hello, my name is [name] and I am [age] years old"


# Create a child class called Student that inherits from Person.

# Student should have:
# - extra property grade
# - __init__ method that uses super()
# - study() method
#   It should print: "[name] is studying"


# Create another child class called Teacher that inherits from Person.

# Teacher should have:
# - extra property subject
# - __init__ method that uses super()
# - teach() method
#   It should print: "[name] is teaching [subject]"


# Polymorphism:
# Override the introduce() method in Student and Teacher.
# Student introduce:
# "I am student [name], my grade is [grade]"
#
# Teacher introduce:
# "I am teacher [name], I teach [subject]"


# Inner Class:
# Inside Student, create an inner class called Laptop.
# Laptop should have:
# - brand property
# - show_laptop() method
#   It should print: "Laptop brand is [brand]"


# Main code:
# - Create one Student object
# - Create one Teacher object
# - Call introduce() for both objects using a loop
# - Change student's age using set_age()
# - Print the updated age using get_age()
# - Create a laptop object for the student
# - Call show_laptop()

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def introduce(self):
        print(
            f"Hello, my name is {self.__name} and I am {self.__age} years old")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.__grade = grade

    def study(self):
        print(f"{super().get_name()} is studying")

    def introduce(self):
        print(f"I am student {super().get_name()}, my grade is {self.__grade}")

    class laptop:
        def __init__(self, brand):
            self.brand = brand

        def show_laptop(self):
            print(f"laptop brand is {self.brand}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.__subject = subject

    def teach(self):
        print(f"{super().get_name()} is teaching {self.__subject}")

    def introduce(self):
        print(f"I am teacher {super().get_name()}, I teach {self.__subject}")


s1 = Student("Dania", 22, "B")
t1 = Teacher("Mr. Samer", 40, "DOS")

for obj in (s1, t1):
    obj.introduce()

s1.set_age(23)
print(s1.get_age())

l1 = s = Student.laptop("HP")
l1.show_laptop()
