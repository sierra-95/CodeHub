#!/usr/bin/env python3
from models.base import Base
class BaseGeometry:
    def integer_validator(self, var_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{var_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{var_name} must be > 0")

class Rectangle(Base,BaseGeometry):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if self.integer_validator("height",height):
            pass
        if self.integer_validator("width",width):
            pass
        if x<0 or y<0:
            raise ValueError(f"value must be >0")
        self.__width=width          
        self.__height=height
        self.__x=x
        self.__y=y    
    @property
    def width (self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y    
    @width.setter  
    def width(self,width):
        self.integer_validator("width",width)
        self.__width=width
    @height.setter
    def height_setter(self,height):
        self.integer_validator("height",height)
        self.__height=height
    @x.setter
    def x(self,x):
        self.integer_validator("x",x)
        self.__x=x
    @y.setter
    def y_setter(self,y):
        self.integer_validator("y",y)
        self.__y=y 

    def area(self):
        return self.__height*self.__width
    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
    def update(self,*args,**kwargs):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
        for key,value in kwargs.items():
            if key == "x":
                self.__x=value
            if key == "y":
                self.__y=value
            if key == "width":
                self.__width=value
            if key == "height":
                self.__height=value
            if key == "id":
                self.id=value

    def to_dictionary(self):
        my_dict={"id":self.id,"width":self.__width,"height":self.__height,"x":self.__x,"y":self.__y}
        return my_dict                        

          