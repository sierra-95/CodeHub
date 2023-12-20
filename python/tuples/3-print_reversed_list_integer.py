#!/usr/bin/env python3
def print_reversed_list_integer(my_list=[]):

    my_list.sort(reverse=True)    
    for i in my_list:
        print("{}".format(i))

     #method 2
def print_reversed_list_integer(my_list=[]):       

    def custom_key(x):
        return -x
    my_list.sort(key=custom_key)
    for i in my_list:
        print("{}".format(i))
