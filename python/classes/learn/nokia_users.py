#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Nokia:
    """collects data about users of Nokia models"""
    def __init__(self,model,version):
        self.type=model
        #self.variable=value
        self.ver=version
    def response(self):
        print(f"Your phone is {self.type} version:{self.ver}")
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
        return print(f"Confirmed {self.__first} {self.__last}")
    #setter method
    def set_name(self,first_name,second_name):
        self.__first=first_name
        self.__last=second_name

#class Users inherited everything from Nokia including response()
user1=Users("Michael","Machohi","Lumia","5.0")   
user1.get_name()
user1.response()
#note the diffrem=nce of using class Nokia alone
phone1=Nokia("samsung galaxy","3.0")
phone1.response()
#setting a value
user1.set_name("James","Gathirwa")
user1.get_name()