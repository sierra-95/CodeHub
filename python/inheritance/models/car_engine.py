#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class car_engine:

    def __init__(self,model,version):
        self.type=model
        self.year=version

    def get_car_version(self):
        return print(f"Your car is {self.type} and version: {self.year}")
class customer_details(car_engine):
    def __init__(self,first_name,second_name,model,version):
        super().__init__(model,version) 
        #private attrb
        self.__first=first_name
        self.__second=second_name   

    def get_details(self):
        return print(f"{self.__first}, {self.__second}")
    def all_details(self):
        return print(f"Dear {self.__first} {self.__second}, your car is {self.type} and version:{self.year}")
    def update_details(self,first_name,second_name):
        self.__first=first_name
        self.__second=second_name


user_1= customer_details("Michael","Machohi","Toyota","supra")
user_1.all_details()
user_1.get_car_version()
user_1.update_details("John","Doe")
user_1.all_details()