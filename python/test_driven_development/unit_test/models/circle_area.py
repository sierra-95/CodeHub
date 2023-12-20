#!/usr/bin/env python3
from math import pi

def circle_areas(r):
    try:
        if type(r) in [int,float]:            
            if  r < 0 :
                raise ValueError
            else: 
                return (r**2)*pi
        elif type(r) in [str]:
            raise TypeError
    except TypeError:
        print("No names allowed")
        return ("Try again")
    except ValueError:
        print("Negative numbers not allowed") 
        return ("Try again")  
print(circle_areas(-2))


