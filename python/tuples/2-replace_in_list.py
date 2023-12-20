#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def replace_in_list(my_list, idx, element):
    
    if idx > len(my_list) and idx < 0 :
        return my_list
    else:
        newlist=my_list.copy()
        newlist[idx]=element
        return newlist