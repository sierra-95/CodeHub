#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class car:

    def __init__(self,make,model):
        self.making=make
        self.modelling=model
#myobject.method()
#myclass.method(myobject)

#car.start_engine(my_car)
#                   |-->self
    def start_engine(self):
        print(f"Engine of {self.making} {self.modelling} started")

    def honk(self):
        print(f"{self.making} is honking")    

my_car1=car("Toyota","camry")
my_car1.start_engine()
my_car2=car("Volkswagen","GTI")
my_car2.honk()