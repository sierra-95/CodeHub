#!/usr/bin/env python3

def append_write(filename="", text=""):
    with open(filename,mode="a",encoding="utf-8") as file:
        #mode="a" will create the file if not exist
        #it will then append content
        file.write(text)
        return len(text)