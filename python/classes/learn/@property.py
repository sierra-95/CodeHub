class Circle:
    def __init__(self, radius):
        self._radius = radius  # Note the underscore, indicating it's a "protected" attribute.

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative.")

    @property
    def area(self):
        return 3.14159265359 * self._radius ** 2
circle = Circle(5)
print(circle.radius)  # Accessing the radius property.
circle.radius = 10    # Modifying the radius property.
print(circle.area)    # Accessing the area property.
