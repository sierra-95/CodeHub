class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating objects and calculating areas
circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)

print("Circle Area:", circle.area())  # Output: Circle Area: 78.5
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
