#!/usr/bin/env python3
def say_my_name(first_name, last_name=""):
    if first_name == str(first_name) and last_name==str(last_name):
        return f"My name is {first_name} {last_name}"
    else:
        raise TypeError("first_name must be a string or last_name must be a string")








#Write a function that prints My name is <first name> <last name>
#Prototype: def say_my_name(first_name, last_name=""):
#first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string
#You are not allowed to import any module