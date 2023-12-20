#!/usr/bin/env python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
       
    def integer_validator(self, name, value):
        if value == str(value) or value == True:
            raise TypeError("<name> must be an integer")
        elif value != int(value):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
        def __init__(self, width, height):
            #you can import a class without super()
            #its however not recomended
            #This non-super() method does not support multiple inheritance
            self.integer_validator("width",width)
            self.integer_validator("height",height)
            self.__height=height
            self.__width=width
        def area(self):
           if self.__height and self.__width:
                return self.__width*self.__height
           else:
               raise Exception("area() is not implemented")
        def __str__(self):
            return (f"[Rectangle] {self.__width}/{self.__height}")   

class square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size",size)
        self.__size=size
    def area(self):
        if self.__size:
            return self.__size*self.__size
        else:
            raise Exception("area() is not implemented")
    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")                                            