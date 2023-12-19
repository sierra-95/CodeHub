#!/usr/bin/env python3
"""filters data types"""
def integer_validator(var_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{var_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{var_name} must be > 0")
    
   
     
print (integer_validator("passed",True))


#Prototype: def add_integer(a, b=98):
#a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
#a and b must be first casted to integers if they are float
#Returns an integer: the addition of a and b
#You are not allowed to import any module