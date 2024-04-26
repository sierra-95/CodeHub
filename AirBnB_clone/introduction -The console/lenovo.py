#!/usr/bin/python3
import uuid
class BaseModel:
    def __init__(self,model,year):
        self.uuid=uuid.uuid4()
        self.__model=model
        self.__year=year
    def laptop(self):
        print(f"Your laptop is a {self.__year} {self.__model}")
    @ property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model=model
        return print(f"model changed to {self.__model}")
class laptop_owners(BaseModel):
    def __init__(self,first_name,last_name,model,year):
        super().__init__(model,year)
        self.__first=first_name
        self.__last=last_name
    @property
    def first(self):
        return self.__first
    @first.setter
    def first(self,first_name):
        if not isinstance(first_name,str):
            raise ValueError("First name must be a string")
        self.__first=first_name
        return print(f"first name changed to {self.__first}")
    @property
    def last(self):
        return self.__last    
    @last.setter
    def last(self,last_name):
        if not isinstance(last_name,str):
            raise ValueError("Last name must be a string")
        self.__last=last_name
        return print(f"last name changed to {self.__last}")

    def __repr__(self):
        return f"{self.__first} {self.__last} owns a {self._BaseModel__year} {self._BaseModel__model}"
    def __str__(self):
        return f"{self.__first} {self.__last} owns a {self._BaseModel__year} {self._BaseModel__model}"            

user1=laptop_owners("John","Doe","Lenovo",2020)
print("User 1 id is",user1.uuid)
user1.laptop()
user2=laptop_owners("Jane","Murphy","HP",2019)
print("User 2 id is",user2.uuid)
print(user1,'while',user2)#uses __str__
user2.first="Peter"
user2.model="Dell"
print(repr(user2))#uses __repr__   NB repr() takes only 1 argument