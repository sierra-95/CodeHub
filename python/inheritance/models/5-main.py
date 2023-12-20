#!/usr/bin/python3
Rectangle = __import__('base_geometry').Rectangle
Square = __import__('base_geometry').square

r = Rectangle(3, 5)

print(r)
print(r.area())

s = Square(13)

print(s)
print(s.area())
