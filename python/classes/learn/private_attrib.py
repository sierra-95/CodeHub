class Car:
    def __init__(self, make, model):
        self.make = make  # Public attribute
        self.__model = model  # Private attribute with double underscore

    def display_make(self):
        return self.make

    def display_model(self):
        return self.__model

# Creating a Car object
my_car = Car("Toyota", "Camry")

# Accessing public attribute
print("Make:", my_car.make)  # Output: Make: Toyota

# Attempting to access private attribute directly (will result in an error)
# print("Model:", my_car.__model)  # This line would produce an error

# Accessing private attribute using name mangling
print("Model:", my_car._Car__model)  # Output: Model: Camry
