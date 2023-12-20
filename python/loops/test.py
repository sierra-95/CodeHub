#!/usr/bin/python3
def alphaconvert(str):
    for i in str:
        c=ord(i)
        if ord(i) >= 97 and ord(i) <=122:
            c=ord(i)-32
        print(chr(c),end="")
    print()  