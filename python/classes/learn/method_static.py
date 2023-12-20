#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Car:
     def __init__(self,model,version):
          self.model=model
          self.version=version
     @staticmethod
     #they dont use self or cls as 1st argument
     def static_method():
          return print("You have a nice car!")

car1=Car("toyota","supra")
print(car1.static_method())          
