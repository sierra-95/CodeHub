#!/usr/bin/env python3

def write_file(filename="", text=""):
    with open(filename,mode="w", encoding="utf-8") as file:
        #mode="w" will create the file if it doesnt exist
        #it will also always overwrite
        file.write(text)
        return len(text)
    
    