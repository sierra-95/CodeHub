#!/usr/bin/python3
#if user allows programmer to print himself
def no_c(my_string):
    for i in my_string:
        c=ord(i)
        if c != 99 and c != 67:
            print(chr(c),end="")
    print()        
no_c("Best school")
no_c("Chicago")
no_c("C is fun")

#if user calls and prints the function himself
def no_c(my_string):
    string=""
    for i in my_string:
        c=ord(i)
        if c != 99 and c != 67:
            string+=chr(c)
    return string 


        
    