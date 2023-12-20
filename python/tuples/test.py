#!/usr/bin/python3
def no_c(my_string):
    string=""
    for i in my_string:
        c=ord(i)
        if c != 99 and c != 67:
            string+=chr(c)
    return string            
           




print(no_c("Best school"))
print(no_c("Chicago"))
print(no_c("C is fun"))

        
        
    