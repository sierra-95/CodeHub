#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nokia:
    """collects data about users of Nokia models"""
    def __init__(self,model,version):
        self.type=model
        #self.variable=value
        self.ver=version
    def response(self):
        return f"Your phone is {self.type} version:{self.ver}"
#inheriting class Nokia
class Users(Nokia):
    """prints users of specific phone types"""
    def __init__(self,first_name,second_name,model,version):
        #importing class Nokia
        super().__init__(model,version)
        self.__first=first_name
        self.__last=second_name
    #getter method
    def get_name(self):
        return f"Confirmed {self.__first} {self.__last}"
    #setter method
    def set_name(self,first_name,second_name):
        self.__first=first_name
        self.__last=second_name

