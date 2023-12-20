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
                                
    def __str__(self):
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return (str1)
        for i in range(0, self.__height):
            for j in range(self.__width):
                str1 += "#"
            if i is not (self.__height - 1):
                str1 += '\n'
        return (str1)







