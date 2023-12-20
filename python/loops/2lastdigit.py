#!/usr/bin/python3

def lastdigit(number):
    print("{:d}".format(abs(number)%10),end="")
    return(abs(number)%10)
