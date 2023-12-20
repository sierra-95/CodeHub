#!/usr/bin/python3
uppercase = __import__('8-uppercase').uppercase
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("upper" if uppercase("H") else "lower"))
print("A is {}".format("lower" if uppercase("A") else "lower"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))