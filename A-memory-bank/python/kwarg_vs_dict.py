#!/usr/bin/env python3
#stores items in dictionary format
def my_func(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

my_func(fruite="apple",quantity=3,color="red")
#to note
#when storing values in dictionary we use this format:
a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
#however when passing a dictionary values to a function we use the above shown method of "var=value"

def my_func2(self,*args,**kwargs):
    for key,value in kwargs.items():
            if key == "x":
                self.__x=value
            if key == "y":
                self.__y=value
            if key == "width":
                self.__width=value
            if key == "height":
                self.__height=value
            if key == "id":
                self.id=value            
