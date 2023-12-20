#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Rectangle:
    def __init__(self,width=0,height=0):
        #if integer
        if width== int(width) and  height== int(height): 
            if width >= 0 and height >=0 :
                self.__width=int(width)
                self.__height=int(height)
        #if less than zero       
        elif width==int(width) and height==int(height):
            if width < 0 and height < 0:
                raise ValueError("size must be >=0")
        #non integer      
        else: 
            raise TypeError("size must be integer")
         
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width=value  
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height=value    
    def perimeter(self):
        if self.__height==0 or self.__width==0:
            return None
        else:
            return 2*(self.__height+self.__width)
    def area(self):
        return (self.__height*self.__width)





#Instantiation with optional width and height: def __init__(self, width=0, height=0):
#Public instance method: def area(self): that returns the rectangle area
#Public instance method: def perimeter(self): that returns the rectangle perimeter:
#if width or height is equal to 0, perimeter is equal to 0