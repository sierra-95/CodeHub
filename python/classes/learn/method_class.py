#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Car:
    #concept1 :class atributes. Are declared on first line
    class_attribute = "I am a class attribute"

    def __init__(self, make_model):
        self.make_model=make_model

    #concept2 : class methods
    @classmethod
    #takes cls as the first argument
    def class_method(cls):
        return print(f"You are? {cls.class_attribute}") 
    #it can only print a class attribute since class methods are bound to the class
    #                                    ------------------------------------------   
    
obj1=Car("toyota")
#printing the attribute
print(obj1.class_attribute)
#printing the method
print(obj1.class_method())