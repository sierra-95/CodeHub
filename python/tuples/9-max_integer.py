#!/usr/bin/env python3
def max_integer(my_list=[]):
    my_list.sort(reverse=False)
    c=my_list[len(my_list)-1]
    return c         
