#!/usr/bin/python3
# -*- coding: utf-8 -*-#
if __name__=="__main__":
    from sys import argv
    print(len(argv)-1,"arguments:")
    for i in range(1,len(argv)):
        if len(argv) > 1:   
            print("{}: {}".format(i,argv[i]))





  
    