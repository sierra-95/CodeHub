#!/usr/bin/env python3
def add_integer(a,b=98):
    try:
       if a == str(a) or b == str(b):
          raise TypeError 
    
       if type(a) or type(b) in [int,float]:
           return int(a)+int(b)
       else:
          raise TypeError
    except TypeError:
     return ("a must be an integer or b must be an integer")   










#Prototype: def add_integer(a, b=98):
#a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
#a and b must be first casted to integers if they are float
#Returns an integer: the addition of a and b
#You are not allowed to import any module