#!/usr/bin/env python3
#just like tuples/lists
# *arg is used to pass a variable length list
def my_func(*args):
    my_list=[] 
    for i in args:
        my_list.append(i)
        print(i)
    print(my_list)  #trying to show that *args stores items in terms of lists  

my_func("apple","banana","cherry")        