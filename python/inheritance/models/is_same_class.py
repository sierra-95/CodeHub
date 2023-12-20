#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_same_class(obj, a_class):

    #if type(obj) == a_class:
        #return True
    #else:
        #return False
    #isinstance not only checks the type()
    # it cheks what the object is an instance of
    # python, everything is object: int,float,str,lists,tuples..etc   
    if isinstance(obj,a_class) is True:
        return True
    else:
        return False    