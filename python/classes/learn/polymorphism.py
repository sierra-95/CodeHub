#!/usr/bin/env python3
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects of different classes
dog = Dog()
cat = Cat()

# Using polymorphism to call the 'speak' method on different objects
animals = [dog, cat]
#animals is a list

for i in animals:
    print(i.speak())
# Output: Woof!
#         Meow!
