#!/usr/bin/env python3

class car:
     def __init__(self,model,version):
          self.type=model
          self.ver=version
     def get_name(self):
          return self.type
     def set_name(self,model,version):
          self.type=model
          self.ver=version          
     def __repr__(self):
          return f"Asked for {self.type} model:{self.ver}"

car1=car("toyota","supra")
print(car1)          