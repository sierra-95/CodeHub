#!/usr/bin/env python3
class Student:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    # Getter method for name
    def get_name(self):
        return self._name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Setter method for age
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

# Creating a Student object
student1 = Student("Alice", 20)

# Using getter methods to access attributes
print("Name:", student1.get_name())  # Output: Name: Alice
print("Age:", student1.get_age())    # Output: Age: 20

# Using setter methods to modify attributes
student1.set_name("Bob")
student1.set_age(21)
# Accessing modified attributes
print("Name:", student1.get_name())  # Output: Name: Bob
print("Age:", student1.get_age())    # Output: Age: 21
