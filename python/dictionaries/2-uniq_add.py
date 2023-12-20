#!/usr/bin/env python3
from functools import reduce
def uniq_add(my_list=[]):
    uniq=[]
    uniq=set(my_list)
    total=lambda x,y: x+y
    result=reduce(total,uniq)
    return result







