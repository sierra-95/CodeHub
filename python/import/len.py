#!/usr/bin/python3
import sys
print("File name:{}".format(sys.argv[0]))
print("Argument count{:d}".format(len(sys.argv)))
#excluding name of program
print("Argument count{:d}".format(len(sys.argv)-1))
print("Argument list:{}".format(str(sys.argv)))
