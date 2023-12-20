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
        area=self.__size*self.__size
        return area

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,value):
        self.__size=value
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}". format("#"), end="")
            print()    


#Public instance method: def my_print(self): that prints in stdout the square with the character #:
#if size is equal to 0, print an empty line        