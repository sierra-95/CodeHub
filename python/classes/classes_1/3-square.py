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








#Public instance method: def area(self): that returns the current square area