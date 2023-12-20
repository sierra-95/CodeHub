#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 50):
        if i % 3 == 0 and i % 5 == 0:
            if i%2==0:
                 print(i,"=",i/6,"*", 3,"*",2)
            else:
                 print(i,"=",i/3,"*",3)                          
        elif i % 3 == 0:
            if i%2==0:
                 print(i,"=",i/6,"*", 3,"*",2)
            else:
                 print(i,"=",i/3,"*", 3)     
           
        elif i % 5 == 0:
            if i%10==0:
                 print(i,"=",i/2,"*",2)
                 if i!=10:
                       print("check for power of",i/2)
            else:
                print(i,"=",i/5,"*" ,5)  
                               
        else:
            print(i)

fizzbuzz()            

