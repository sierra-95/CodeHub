#!/usr/bin/env python3
from models.base import Base
class BaseGeometry:
    def integer_validator(self, var_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{var_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{var_name} must be > 0")

class Square(Base,BaseGeometry):
    def __init__(self,size, x=0, y=0, id=None):
        super().__init__(id)
        if self.integer_validator("size",size):
            pass
        
        if x<0 or y<0:
            raise ValueError(f"value must be >0")
        self.__size=size          
        self.__x=x
        self.__y=y    
    @property
    def size (self):
        return self.__size
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y    
    @size.setter  
    def size(self,size):
        self.integer_validator("size",size)
        self.__size=size
    @x.setter
    def x(self,x):
        self.integer_validator("x",x)
        self.__x=x
    @y.setter
    def y_setter(self,y):
        self.integer_validator("y",y)
        self.__y=y 

    def area(self):
        return self.__size*self.__size
    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
    def update(self,*args,**kwargs):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__size = args[1]
        if len(args) >= 3:
            self.__x = args[2]
        if len(args) >= 4:
            self.__y = args[3]

        for key,value in kwargs.items():
            if key == "x":
                self.__x=value
            if key == "y":
                self.__y=value
            if key == "size":
                self.__size=value
            if key == "id":
                self.id=value 
    def to_dictionary(self):
        my_dict={"id":self.id,"size":self.__size,"x":self.__x,"y":self.__y}
        return my_dict
        

