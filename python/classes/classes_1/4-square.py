#!/usr/bin/env python3
class Square:
    """defines a square"""
    def __init__(self,size=0):
        if size== int(size) and size >= 0:
            self.__size=int(size)
                
        elif size==int(size) and size < 0 :
            raise ValueError("size must be >=0")
              
        else: 
            raise TypeError("size must be integer")    
    

    def area(self):
        if self.__size == str(self.__size):
            pass
        else:    
            area=self.__size*self.__size
            return area

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        self.__size=value
#property def size(self): to retrieve it
#property setter def size(self, value): to set it:
#size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
#if size is less than 0, raise a ValueError exception with the message size must be >= 0
#Instantiation with optional size: def __init__(self, size=0):
#Public instance method: def area(self): that returns the current square area
#You are not allowed to import any module